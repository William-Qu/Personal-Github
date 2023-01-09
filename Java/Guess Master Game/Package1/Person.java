package Package1;

public class Person extends Entity{
	private String gender;
	
	public Person(String name, Date birthDate, double diff, String gend) {
		super(name, birthDate, diff);
		this.gender = gend;
	}
	
	public Person(Person pers) {
		super(pers.getName(), pers.getBorn(), pers.getDifficulty());
		this.gender = pers.gender;
	}
	
	public Person clone() {
		Person copy = new Person(getName(), getBorn(), getDifficulty(), this.gender);
		return copy;
	}
	
	public String getGender() {
		return gender;
	}
	
	public String entityType() {
		return "This entity is a person!";
	}
}
