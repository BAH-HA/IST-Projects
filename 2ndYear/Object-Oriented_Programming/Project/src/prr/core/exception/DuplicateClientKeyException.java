package prr.core.exception;

/** Exception thrown when a client key is duplicated. */
public class DuplicateClientKeyException extends Exception {
  
  private final String _key;

  public DuplicateClientKeyException(String key) {
    this._key = key;
  }

  public String key() {
    return _key;
  }
}
