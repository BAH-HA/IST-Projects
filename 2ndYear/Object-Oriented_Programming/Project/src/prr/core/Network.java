package prr.core;

import java.io.Serializable;
import java.io.IOException;
import java.util.Collections;
import java.util.List;
import java.util.ArrayList;
import java.util.TreeMap;
import java.util.Map;
import java.util.Collection;

import prr.core.exception.UnrecognizedEntryException;
import prr.core.exception.DuplicateClientKeyException;
import prr.core.exception.UnknownClientKeyException;
import prr.core.Client;
import prr.core.Terminal;

// FIXME add more import if needed (cannot import from pt.tecnico or prr.app)

/**
 * Class Store implements a store.
 */
public class Network implements Serializable {

  /** Serial number for serialization. */
  private static final long serialVersionUID = 202208091753L;

  private final Map<String, Client> _clients = new TreeMap<>();

  private final Map<String, Terminal> _terminals = new TreeMap<>();

  /**
   * Read text input file and create corresponding domain entities.
   * 
   * @param filename name of the text input file
   * @throws UnrecognizedEntryException if some entry is not correct
   * @throws IOException if there is an IO erro while processing the text file
   */
  void importFile(String filename) throws UnrecognizedEntryException, IOException /* FIXME maybe other exceptions */  {
    //FIXME implement method
  }

  /**
   * Registers a client
   */
  public Client registerClient(String name, int taxNumber, String key) 
          throws DuplicateClientKeyException {
      
    if (this._clients.containsKey(key)) {
      throw new DuplicateClientKeyException(key);
    }

    Client c = new Client(name, taxNumber, key);
    this._clients.put(key, c);
    return c;
  }
  
  public Collection<Client> getAllClients() {
    return this._clients.values();
  }

  public Client getClient(String key) throws UnknownClientKeyException {
    Client c = this._clients.get(key);
    if (c == null) {
      throw new UnknownClientKeyException(key);
    }
    return c;
  }

  /**
   * Starts a Text Communication
   *
   public void sendTextCommunication(form:Terminal from, String toKey, String msg)
  */

  /**
   * Starts an Interactive Communication
   *
  public void startInteractiveCommunication(from:Terminal, String toKey, String type) {
  */
}

