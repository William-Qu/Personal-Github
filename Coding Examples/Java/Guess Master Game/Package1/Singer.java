package Package1;

public class Singer extends Person{
	private String debutAlbum;
	private Date debutAlbumReleaseDate;
	
	public Singer(String name, Date birthDate, double diff, String gend, String deb, Date dat) {
		super(name, birthDate, diff, gend);
		this.debutAlbum = deb;
		this.debutAlbumReleaseDate = dat;
	}
	
	public Singer(Singer sing) {
		super(sing.getName(), sing.getBorn(), sing.getDifficulty(), sing.getGender());
		this.debutAlbum = sing.debutAlbum;
		this.debutAlbumReleaseDate = sing.debutAlbumReleaseDate;
	}
	
	public Singer clone() {
		Singer copy = new Singer(getName(), getBorn(), getDifficulty(), getGender(), debutAlbum, debutAlbumReleaseDate);
		return copy;
	}
	
	public String entityType() {
		return "This entity is a singer!";
	}
}

