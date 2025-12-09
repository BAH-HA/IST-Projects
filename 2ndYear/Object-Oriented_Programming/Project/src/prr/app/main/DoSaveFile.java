package prr.app.main;

import prr.core.NetworkManager;
import prr.core.exception.MissingFileAssociationException;
import pt.tecnico.uilib.forms.Form;
import pt.tecnico.uilib.menus.Command;
import pt.tecnico.uilib.menus.CommandException;
import java.io.IOException;

/**
 * Command to save a file.
 */
class DoSaveFile extends Command<NetworkManager> {

  DoSaveFile(NetworkManager receiver) {
    super(Label.SAVE_FILE, receiver);
  }
  
  @Override
  protected final void execute() throws CommandException {
    try {
      if (_receiver.getFilename() == ""){
        Form f = new Form();
        f.addStringField("filename", Message.newSaveAs());
        f.parse();
        _receiver.saveAs(f.stringField("filename")); 
      } else {
        _receiver.save();
      }
    } catch (IOException | MissingFileAssociationException e){
      _display.addLine(e.getMessage());
    }
        
    _display.display();
  }
}
