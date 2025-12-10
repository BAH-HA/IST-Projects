%{
//-- don't change *any* of these: if you do, you'll break the compiler.
#include <algorithm>
#include <memory>
#include <cstring>
#include <cdk/compiler.h>
#include <cdk/types/types.h>
#include ".auto/all_nodes.h"
#define LINE                         compiler->scanner()->lineno()
#define yylex()                      compiler->scanner()->scan()
#define yyerror(compiler, s)         compiler->scanner()->error(s)
//-- don't change *any* of these --- END!
%}

%parse-param {std::shared_ptr<cdk::compiler> compiler}

%union {
  //--- don't change *any* of these: if you do, you'll break the compiler.
  YYSTYPE() : type(cdk::primitive_type::create(0, cdk::TYPE_VOID)) {}
  ~YYSTYPE() {}
  YYSTYPE(const YYSTYPE &other) { *this = other; }
  YYSTYPE& operator=(const YYSTYPE &other) { type = other.type; return *this; }

  std::shared_ptr<cdk::basic_type> type;        /* expression type */
  //-- don't change *any* of these --- END!

  int                   i;          /* integer value */
  double                d;
  std::string          *s;          /* symbol name or string literal */
  cdk::basic_node      *node;       /* node pointer */
  cdk::sequence_node   *sequence;
  cdk::expression_node *expression; /* expression nodes */
  cdk::lvalue_node     *lvalue;
  til::block_node      *block;
  std::vector<std::shared_ptr<cdk::basic_type>> *type_vec;
};

%token <i> tINTEGER
%token <d> tDOUBLE
%token <s> tIDENTIFIER tSTRING
%token tLOOP tIF tPRINT tREAD tBEGIN tEND tPROGRAM tFUNCTION tTYPE_VOID
%token tWHILE tBLOCK tTYPE_INT tTYPE_STRING tTYPE_NULL
%token tPRINTLN tSIZEOF tRETURN tSTOP tNEXT tNULL tINDEX tTYPE_DOUBLE tSET
%token tFORWARD tEXTERNAL tPUBLIC tVAR tPRIVATE tOBJECTS tPONTEIRO
%token tOR tAND tNOT tRECURSIVE tADDRESS

%nonassoc tIFX
%nonassoc tELSE tELSEIF

%right '='
%left tGE tLE tEQ tNE '>' '<'
%left '+' '-' 
%left '*' '/' '%'
%nonassoc tUNARY

%type <node>  instruction program declaration ifelse vardeclaration func_arg 
%type <sequence> instructions declarations vardeclarations func_args //exprs 
%type <type>  type_literal function_type ponteiro_type func_ret_type
%type <type_vec> types
%type <expression> expr func 
%type <lvalue> lval
%type <block> block declarations_instructions

%{
//-- The rules below will be included in yyparse, the main parsing function.
%}
%%

file : vardeclarations program                         { compiler->ast(new cdk::sequence_node(LINE, $2, $1)); }
     | vardeclarations                                 { compiler->ast($1); }
     | program                                         { compiler->ast(new cdk::sequence_node(LINE, $1)); }
     |                                                 { compiler->ast(new cdk::sequence_node(LINE)); }
     ;

vardeclarations : vardeclarations vardeclaration       { $$ = new cdk::sequence_node(LINE, $2, $1);}
                | vardeclaration                       { $$ = new cdk::sequence_node(LINE, $1);}
                ;

vardeclaration : '('tFORWARD type_literal  tIDENTIFIER     ')'      { $$ = new til::declaration_node(LINE, tFORWARD,  *$4,$3, nullptr); delete $4; }
|              | '('tEXTERNAL  type_literal  tIDENTIFIER   ')'      { $$ = new til::declaration_node(LINE, tEXTERNAL,  *$4,$3, nullptr); delete $4; }
               | '('tPUBLIC  type_literal  tIDENTIFIER     ')'      { $$ = new til::declaration_node(LINE, tPUBLIC,  *$4,$3, nullptr); delete $4; }
               | '('tPUBLIC  type_literal  tIDENTIFIER expr')'      { $$ = new til::declaration_node(LINE, tPUBLIC,  *$4,$3, $5); delete $4; }
               | '('tPUBLIC tIDENTIFIER expr ')'                    { $$ = new til::declaration_node(LINE, tPUBLIC,  *$3, nullptr, $4); delete $3; }
               | declaration                                        { $$ = $1; }
               ;

program : '(' tPROGRAM declarations_instructions ')'   {$$ = new til::program_node(LINE, $3);}
        ;

declarations_instructions : declarations instructions  { $$ = new til::block_node(LINE, $1, $2); }
                          | declarations               { $$ = new til::block_node(LINE, $1, new cdk::sequence_node(LINE)); }
                          | instructions               { $$ = new til::block_node(LINE, new cdk::sequence_node(LINE), $1); }
                          |                            { $$ = new til::block_node(LINE, new cdk::sequence_node(LINE), new cdk::sequence_node(LINE)); }
                          ;

declarations : declarations declaration                { $$ = new cdk::sequence_node(LINE, $2, $1); }
             | declaration                             { $$ = new cdk::sequence_node(LINE, $1); }
             ;

declaration : '(' type_literal  tIDENTIFIER  ')'               { $$ = new til::declaration_node(LINE, tPRIVATE,  *$3,$2, nullptr); delete $3; }
            | '(' type_literal  tIDENTIFIER expr  ')'          { $$ = new til::declaration_node(LINE, tPRIVATE,  *$3,$2, $4); delete $3; }
            | '(' tVAR  tIDENTIFIER expr   ')'         { $$ = new til::declaration_node(LINE, tPRIVATE,  *$3, cdk::primitive_type::create(0, cdk::TYPE_UNSPEC), $4); delete $3; }
            ;

type_literal : tTYPE_INT                                       { $$ = cdk::primitive_type::create(4, cdk::TYPE_INT);}
             | tTYPE_DOUBLE                                    { $$ = cdk::primitive_type::create(8, cdk::TYPE_DOUBLE);}
             | tTYPE_STRING                                    { $$ = cdk::primitive_type::create(4, cdk::TYPE_STRING);}
             | function_type                                   { $$ = $1; }
             | ponteiro_type                                   { $$ = $1; }
             | tTYPE_VOID                                      { $$ = cdk::reference_type::create(4, cdk::primitive_type::create(0, cdk::TYPE_VOID)); }
             ;

function_type : '(' func_ret_type '(' types ')' ')'                      { $$ = cdk::functional_type::create(*$4, $2); delete $4;}
              | '(' func_ret_type ')'                                    { $$ = cdk::functional_type::create($2); } 
              ;


types : types type_literal                                     { $$ = $1; $$->push_back($2); } 
      | type_literal                                           { $$ = new std::vector<std::shared_ptr<cdk::basic_type>>(1, $1); } 
      ;

ponteiro_type : type_literal tPONTEIRO                                               { $$ = cdk::reference_type::create(4, $1); }
              ;

instructions : instruction                             { $$ = new cdk::sequence_node(LINE, $1); } 
             | instructions instruction                { $$ = new cdk::sequence_node(LINE, $2, $1); }
             ;

instruction : expr                                     { $$ = new til::evaluation_node(LINE, $1); }
     | '(' tPRINT instructions ')'                     { $$ = new til::print_node(LINE, $3, false); }
     | '(' tPRINTLN instructions ')'                   { $$ = new til::print_node(LINE, $3, true); }
     | '(' tIF  expr  instructions %prec tIFX ')'      { $$ = new til::if_node(LINE, $3, $4); }
     | '(' tIF  expr  instructions ifelse ')'          { $$ = new til::if_else_node(LINE, $3, $4, $5); }
     | '(' tLOOP  expr  instructions ')'               { $$ = new til::while_node(LINE, $3, $4); }
     | '(' instructions ')'                            { $$ = $2; }
     | '(' tREAD lval ')'                              { $$ = new til::read_node(LINE, $3); }
     | '(' tRETURN expr ')'                            { $$ = new til::return_node(LINE, $3); }
     | '(' tRETURN ')'                                 { $$ = new til::return_node(LINE, nullptr); }
     | '(' tSTOP tINTEGER ')'                          { $$ = new til::stop_node(LINE, $3); }
     | '(' tSTOP ')'                                   { $$ = new til::stop_node(LINE); }
     | '(' tNEXT tINTEGER ')'                          { $$ = new til::next_node(LINE, $3); }
     | '(' tNEXT ')'                                   { $$ = new til::next_node(LINE); } 
     | '(' tBLOCK declarations_instructions')'                             { $$ = $3;}
     ;

block : declarations instructions                      { $$ = new til::block_node(LINE, $1, $2); }
      | declarations                                   { $$ = new til::block_node(LINE, $1, new cdk::sequence_node(LINE)); }
      | instructions                                   { $$ = new til::block_node(LINE, new cdk::sequence_node(LINE), $1); }
      | /* vazio */                                    { $$ = new til::block_node(LINE, new cdk::sequence_node(LINE), new cdk::sequence_node(LINE)); }
      ;



ifelse : tELSE instructions                            { $$ = $2;}
       | tELSEIF  expr  instructions %prec tIFX        { $$ = new til::if_node(LINE, $2, $3);}
       | tELSEIF  expr  instructions ifelse            { $$ = new til::if_else_node(LINE, $2, $3, $4);}
       ;

expr : tINTEGER                                        { $$ = new cdk::integer_node(LINE, $1); }
     | '(' expr instructions ')'                               { $$ = new til::function_call_node(LINE, $2, $3); }
     | '(' expr instructions ')'                               { $$ = new til::function_call_node(LINE, $2, new cdk::sequence_node(LINE)); }     
     | '('tRECURSIVE instructions ')'                          { $$ = new til::function_call_node(LINE, nullptr, $3); }
     | '('tRECURSIVE ')'                               { $$ = new til::function_call_node(LINE, nullptr, new cdk::sequence_node(LINE)); }     
     | tDOUBLE                                         { $$ = new cdk::double_node(LINE, $1); }
     | tSTRING                                         { $$ = new cdk::string_node(LINE, $1); }
     | tNULL                                           { $$ = new til::null_node(LINE); }
     | '(' tSIZEOF expr ')'                                    { $$ = new til::sizeof_node(LINE, $3); }
     | '(' '-' expr %prec tUNARY ')'                          { $$ = new cdk::unary_minus_node(LINE, $3); }
     | '(' '+' expr %prec tUNARY ')'                          { $$ = new cdk::unary_plus_node(LINE, $3); }
     | '(' tNOT expr ')'                                      { $$ = new cdk::not_node(LINE, $3);}
     | '(' tAND expr expr ')'                                  { $$ = new cdk::and_node(LINE, $3, $4);}
     | '(' tOR expr expr ')'                                   { $$ = new cdk::or_node(LINE, $3, $4);}
     | '(' '+' expr expr ')'                                   { $$ = new cdk::add_node(LINE, $3, $4); }
     | '(' '-' expr expr ')'                                   { $$ = new cdk::sub_node(LINE, $3, $4); }
     | '(' '*' expr expr ')'                                   { $$ = new cdk::mul_node(LINE, $3, $4); }
     | '(' '/' expr expr ')'                                   { $$ = new cdk::div_node(LINE, $3, $4); }
     | '(' '%' expr expr ')'                                   { $$ = new cdk::mod_node(LINE, $3, $4); }
     | '(' '<' expr expr ')'                                   { $$ = new cdk::lt_node(LINE, $3, $4); }
     | '(' '>' expr expr ')'                                   { $$ = new cdk::gt_node(LINE, $3, $4); }
     | '(' tGE expr expr ')'                                   { $$ = new cdk::ge_node(LINE, $3, $4); }
     | '(' tLE expr expr ')'                                   { $$ = new cdk::le_node(LINE, $3, $4); }
     | '(' tNE expr expr ')'                                   { $$ = new cdk::ne_node(LINE, $3, $4); }
     | '(' tEQ expr expr ')'                                   { $$ = new cdk::eq_node(LINE, $3, $4); }
     | lval                                            { $$ = new cdk::rvalue_node(LINE, $1); }
     | '(' lval ')'                                    { $$ = new cdk::rvalue_node(LINE, $2); }
     | '(' tADDRESS lval ')'                                       { $$ = new til::address_of_node(LINE, $3); }
     | '(' tADDRESS '(' lval ')' ')'                                       { $$ = new til::address_of_node(LINE, $4); }
     | '(' tSET lval expr ')'                                  { $$ = new cdk::assignment_node(LINE, $3, $4); }
     | '(' tSET '(' lval ')' expr')'                           { $$ = new cdk::assignment_node(LINE, $4, $6); }
     | '(' tOBJECTS expr ')'                                   { $$ = new til::alloc_node(LINE, $3); }
     | func                                            { $$ = $1; }
     ;

lval : tIDENTIFIER                                     { $$ = new cdk::variable_node(LINE, $1); }
     | tINDEX expr expr                                { $$ = new til::index_node(LINE, $2, $3); }
     ;

func_args : func_args func_arg                         { $$ = new cdk::sequence_node(LINE, $2, $1);}
          | func_arg                                   { $$ = new cdk::sequence_node(LINE, $1);}
          ;

func_arg : '(' type_literal tIDENTIFIER ')'                    { $$ = new til::declaration_node(LINE, tPRIVATE,  *$3, $2, nullptr); delete $3; }
         ;

func : '(' tFUNCTION '(' func_ret_type ')' declarations_instructions ')'               { $$ = new til::function_node(LINE, $4, new cdk::sequence_node(LINE), $6); } 
     | '(' tFUNCTION '(' func_ret_type declarations ')' declarations_instructions ')'     { $$ = new til::function_node(LINE, $4, $5, $7); } 
     ; 


func_ret_type : type_literal { $$ = $1; } 
     | tTYPE_VOID    { $$ = cdk::primitive_type::create(0, cdk::TYPE_VOID); }
                 ;
%%

