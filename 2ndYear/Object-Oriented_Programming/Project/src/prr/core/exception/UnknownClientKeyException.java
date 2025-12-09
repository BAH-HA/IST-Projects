package prr.core.exception;

/**
 * Exception for unknown clients.
 */
public class UnknownClientKeyException extends Exception {

  /** Search key */
  private String _key;

  public UnknownClientKeyException(String key) {
    this._key = key;
  }

  public String key() {
    return _key;
  }
}