package Package1;

public abstract class Entity {
	private String name;
	private Date born;
	private double difficulty;
	
	public Entity(String name, Date birthDate, double diff) {
		this.name = name;
		this.born = new Date(birthDate); //no privacy leak
		this.difficulty = diff;
	}
	
	public Entity(Entity entity) {
		this.name = entity.name;
		this.born = new Date(entity.born); //no privacy leak
		this.difficulty = entity.difficulty;
	}

	public String getName() {
		return name;
	}

	public Date getBorn() {
		return new Date(born);
	}
	
	public double getDifficulty() {
		return difficulty;
	}
	
	public double getAwardedTicketNumber() {
		return (difficulty * 100);
	}
	
	//Game Messages, might not have invoked entityType() correctly
	public String welcomeMessage() {
		return ("Welcome! Let's start the game! This entity is a " + entityType());
	}
	
	public String closingMessage() {
		return ("Congratulations! The detailed information of the entity you guess is: " + toString());
	}
	
	//Abstract Methods
	public abstract String entityType();
	
	public abstract Entity clone();
	
	public String toString() {
		String diff = String.valueOf(difficulty);
		return "Name: "+name+"\n"+"Born at: "+born.toString()+"\n"+"Difficulty: "+diff+"\n";
	}
}
