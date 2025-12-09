package prr.app.terminals;

import prr.core.Network;
import prr.app.exception.DuplicateTerminalKeyException;
import prr.app.exception.InvalidTerminalKeyException;
import prr.app.exception.UnknownClientKeyException;
import pt.tecnico.uilib.menus.Command;
import pt.tecnico.uilib.menus.CommandException;
//FIXME add more imports if needed

/**
 * Register terminal.
 */
class DoRegisterTerminal extends Command<Network> {

  DoRegisterTerminal(Network receiver) {
    super(Label.REGISTER_TERMINAL, receiver);
    addStringField("terminalkey", Message.terminalKey());
    addOptionField("terminalType", Message.terminalType(), "BASIC","FANCY");
    addStringField("clientKey", Message.clientKey());
  }

  @Override
  protected final void execute() throws CommandException {
    try {
      _receiver.registerTerminal(stringField("terminalkey"), optionField("terminalType"), stringField("clientKey"));
    } catch (prr.core.exception.DuplicateTerminalKeyException e) {
      throw new DuplicateTerminalKeyException(e.key());
    } catch (prr.core.exception.InvalidTerminalKeyException e) {
      throw new InvalidTerminalKeyException(e.key());
    } catch (prr.core.exception.UnknownClientKeyException e) {
      throw new UnknownClientKeyException(e.key());
    }
  }
}
