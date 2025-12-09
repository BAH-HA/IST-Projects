package prr.app.client;

import prr.core.Network;
import prr.app.exception.DuplicateClientKeyException;
import pt.tecnico.uilib.menus.Command;
import pt.tecnico.uilib.menus.CommandException;

/**
 * Register new client.
 */
class DoRegisterClient extends Command<Network> {

  DoRegisterClient(Network receiver) {
    super(Label.REGISTER_CLIENT, receiver);
    addStringField("key", Message.key());
    addStringField("name", Message.name());
    addIntegerField("taxNumber", Message.taxId());
  }

  @Override
  protected final void execute() throws CommandException {
    try {
      _receiver.registerClient(
              stringField("name"), 
              integerField("taxNumber"), 
              stringField("key")
      );
    } catch (prr.core.exception.DuplicateClientKeyException e) {
      throw new DuplicateClientKeyException(e.key());
    }
  }
}