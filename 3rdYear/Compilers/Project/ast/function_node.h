#include <cdk/ast/expression_node.h>
#include <cdk/ast/basic_node.h>
#include <cdk/ast/sequence_node.h>
#include <cdk/ast/typed_node.h>
#include <cdk/types/basic_type.h>
#include "block_node.h"


namespace til{
    /**
     * Class for describing function nodes
     * 
     */
    class function_node: public cdk::expression_node {
        cdk::sequence_node *_arguments;
        std::shared_ptr<cdk::basic_type> _type;
        til::block_node *_block;

    public:
        function_node(int lineno, std::shared_ptr<cdk::basic_type> type , cdk::sequence_node *arguments, til::block_node *block) :
        cdk::expression_node(lineno), _arguments(arguments), _block(block){
        }
    
    public:
        cdk::sequence_node *arguments(){return _arguments;}
        
        til::block_node *block(){return _block;}

        std::shared_ptr<cdk::basic_type> type(){return _type;}

        void accept(basic_ast_visitor *sp, int lvl){sp->do_function_node(this,lvl);}
    };

}// til