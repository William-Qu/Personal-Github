package Package1;

public class Politician extends Person{
	private String party;
	
	public Politician(String name, Date birthDate, double diff, String gend, String part) {
		super(name, birthDate, diff, gend);
		this.party = part;
	}
	
	public Politician(Politician poli) {
		super(poli.getName(), poli.getBorn(), poli.getDifficulty(), poli.getGender());
		this.party = poli.party;
	}
	
	public Politician clone() {
		Politician copy = new Politician(getName(), getBorn(), getDifficulty(), getGender(), this.party);
		return copy;
	}
	
	public String entityType() {
		return "This entity is a Politician!";
	}
}
