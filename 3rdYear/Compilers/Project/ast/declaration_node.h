#include <cdk/ast/expression_node.h>
#include <cdk/ast/typed_node.h>
#include <cdk/types/basic_type.h>

namespace til {

  /**
   * Class for describing declaration nodes.
   */
  class declaration_node: public cdk::typed_node {
    int _qualifier;
    std::string _identifier;
    std::shared_ptr<cdk::basic_type> _type;
    cdk::expression_node *_initializer;

  public:
    declaration_node(int lineno, int qualifier, std::string &identifier, std::shared_ptr<cdk::basic_type> type, 
          cdk::expression_node *initializer) :
        cdk::typed_node(lineno), _qualifier(qualifier), _identifier(identifier), _type(type), _initializer(initializer) {
        }

  public:
    int qualifier() {return _qualifier;}
    
    const std::string &identifier() {return _identifier;}
    
    cdk::expression_node *initializer() {return _initializer;}

    std::shared_ptr<cdk::basic_type> type() {return _type;}

    void accept(basic_ast_visitor *sp, int level) {sp->do_declaration_node(this, level);}

  };

} // til

