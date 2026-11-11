package Package1;

public class Country extends Entity{
	private String capital;
	
	public Country(String name, Date birthDate, double diff, String cap) {
		super(name, birthDate, diff);
		this.capital = cap;
	}
	
	public Country(Country country) {
		super(country.getName(), country.getBorn(), country.getDifficulty());
		this.capital = country.capital;
	}
	
	public Country clone() {
		Country copy = new Country(getName(), getBorn(), getDifficulty(), this.capital);
		return copy;
	}
	
	public String entityType() {
		return "This entity is a country!";
	}
}
