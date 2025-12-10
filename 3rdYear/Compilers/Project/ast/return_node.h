#pragma once

#include <cdk/ast/basic_node.h>

namespace til {

  /**
   * Class for representing return statements in the AST.
   */
  class return_node : public cdk::basic_node {
    cdk::expression_node *_argument;
  public:
    return_node(int lineno, cdk::expression_node *argument) : cdk::basic_node(lineno), _argument(argument) {
        
    }

    cdk::expression_node *argument() { return _argument; }

    void accept(basic_ast_visitor *sp, int level) override { sp->do_return_node(this, level);
    }
  };

} //til
