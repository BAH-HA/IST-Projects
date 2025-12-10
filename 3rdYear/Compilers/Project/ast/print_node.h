#pragma once

#include <cdk/ast/expression_node.h>

namespace til
{

  /**
   * Class for describing print nodes.
   */
  class print_node : public cdk::basic_node
  {
    cdk::sequence_node *_argument;
    bool _new_line = false;

  public:
    print_node(int lineno, cdk::sequence_node *argument, bool new_line = false) : cdk::basic_node(lineno), _argument(argument), _new_line(new_line)
    {
    }

    cdk::sequence_node *argument() { return _argument; }
    bool new_line() {
      return _new_line;
    }
    void accept(basic_ast_visitor *sp, int level) { sp->do_print_node(this, level); }
  };

} // til
