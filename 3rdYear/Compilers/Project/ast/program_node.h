#pragma once

#include <cdk/ast/basic_node.h>
#include <cdk/ast/sequence_node.h>

namespace til {

  /**
   * Class for describing program nodes.
   */
  class program_node : public cdk::basic_node {
    til::block_node *_statements;

  public:
    program_node(int lineno, til::block_node *statements) :
        cdk::basic_node(lineno), _statements(statements) {
    }

    til::block_node *statements() { return _statements; }

    void accept(basic_ast_visitor *sp, int level) { sp->do_program_node(this, level); }

  };

} // til
