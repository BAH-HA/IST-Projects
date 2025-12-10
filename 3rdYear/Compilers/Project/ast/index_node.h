#include <cdk/ast/expression_node.h>
#include <cdk/ast/lvalue_node.h>

namespace til {

  /**
   * Class for describing pointer index nodes.
   */
  class index_node: public cdk::lvalue_node {
    cdk::expression_node *_name, *_index;

  public:
    index_node(int lineno, cdk::expression_node *name, cdk::expression_node *index) :
        cdk::lvalue_node(lineno), _name(name), _index(index) {
    }

  public:
    cdk::expression_node *name() {return _name;}
    cdk::expression_node *index() {return _index;}

    void accept(basic_ast_visitor *sp, int level) {sp->do_index_node(this, level);}

  };

} // til