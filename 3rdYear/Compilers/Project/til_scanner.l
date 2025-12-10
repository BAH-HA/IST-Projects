%option c++ prefix="til_scanner_" outfile="til_scanner.cpp"
%option stack noyywrap yylineno 8bit debug
%{ 
// make relevant includes before including the parser's tab file
#include <string>
#include <cdk/ast/sequence_node.h>
#include <cdk/ast/expression_node.h>
#include <cdk/ast/lvalue_node.h>
#include "til_parser.tab.h"

// don't change this
#define yyerror LexerError

%}

%x X_STRING COMMENT
%%
yydebug=1; set_debug(1);

";".*                 ; /* ignore comments */

">="                   return tGE; 
"<="                   return tLE; 
"=="                   return tEQ; 
"!="                   return tNE; 

"int"                  return tTYPE_INT;
"double"               return tTYPE_DOUBLE;
"string"               return tTYPE_STRING;
"void"                 return tTYPE_VOID;



"while"                return tWHILE;
"loop"                 return tLOOP;

"program"              return tPROGRAM;

"function"             return tFUNCTION;

"if"                   return tIF; 
"else"                 return tELSE; 
"else if"              return tELSEIF;
"print"                return tPRINT; 
"read"                 return tREAD; 
"begin"                return tBEGIN; 
"end"                  return tEND; 

"~"                    return tNOT;
"&&"                   return tAND;
"||"                   return tOR;

"@"                    return tRECURSIVE;

"?"                    return tADDRESS;

"!"                    return tPONTEIRO;
"objects"              return tOBJECTS;
"sizeof"               return tSIZEOF;
"return"               return tRETURN;
"println"              return tPRINTLN; 
"stop"                 return tSTOP;
"next"                 return tNEXT;
"null"                 return tNULL;
"index"                return tINDEX;
"block"                return tBLOCK;
"var"                  return tVAR;
"forward"              return tFORWARD;
"external"             return tEXTERNAL;
"public"               return tPUBLIC;
"set"                  return tSET;


[A-Za-z][A-Za-z0-9_]*  yylval.s = new std::string(yytext); return tIDENTIFIER;

\"                     yy_push_state(X_STRING); yylval.s = new std::string("");
<X_STRING>\"           yy_pop_state(); return tSTRING;
<X_STRING>\\\"         *yylval.s += yytext + 1;
<X_STRING>.            *yylval.s += yytext;
<X_STRING>\n           yyerror("newline in string");

"/*"                   yy_push_state(COMMENT);
<COMMENT>"*/"          yy_pop_state();
<COMMENT>. | \n             ; // Ignore characters inside comment



[0-9]+                 yylval.i = strtol(yytext, nullptr, 10); return tINTEGER;
[0-9]+(\.[0-9]+)?([eE][-+]?[0-9]+)? { yylval.d = strtod(yytext, nullptr); return tDOUBLE; }


[-()<>=+*/%;{}.]       return *yytext;

[ \t\n]+               ; /* ignore whitespace */

.                      yyerror("Unknown character");

%%
