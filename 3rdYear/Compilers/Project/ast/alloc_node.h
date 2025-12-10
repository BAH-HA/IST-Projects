#pragma once

#include <cdk/ast/unary_operation_node.h>

namespace til {

  /**
   * Class for describing stack allocation nodes.
   */
  class alloc_node: public cdk::unary_operation_node {
  public:
    alloc_node(int lineno, cdk::expression_node *argument) :
        cdk::unary_operation_node(lineno, argument) {
    }

  public:
    void accept(basic_ast_visitor *sp, int level) {
      sp->do_alloc_node(this, level);
    }

  };

} // til