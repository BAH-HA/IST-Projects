package prr.core;

public class Client {

	private String _key;
	private String _name;
	private int _taxNumber;
	//private ClientLevel _level;
	private boolean _receiveNotifications;

	public Client(String name, int taxNumber, String key) {
		_key = key;
		_name = name;
		_taxNumber = taxNumber;
		//this._level = NORMAL;
		_receiveNotifications = true;
	}

	public String getKey() {
		return this._key;
	}

	public String getName() {
		return this._name;
	}

	public int getTaxNumber() {
		return this._taxNumber;
	}

	public String toString(){
        return "CLIENT|" + _key + "|" + _name + "|" + _taxNumber + "| ...";
        // CLIENT|key|name|taxId|type|notifications|terminals|payments|debts
    }
	
}