package bookmanagementsystem;

public interface Subject {
	public void removeObserver(Observer observer);
	public void registerObserver(Observer observer);
	public void notifyObservers();
}
