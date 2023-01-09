package Package1;

import java.util.Random;
import java.util.Scanner;

public class GuessMaster {
	private int numOfEntities;
	private Entity[] entities; 
	
	public GuessMaster() {
		numOfEntities = 0;
		entities = new Entity[100]; 
	}

	public void addEntity(Entity entity) {
		entities[numOfEntities++] = entity.clone();
	}
	
	public void playGame(int entityId) {
		Entity entity = entities[entityId];
		playGame(entity);
	}
	
	public void playGame(Entity entity) {
		System.out.printf("\nGuess %s's birthday\n", entity.getName());
		System.out.println("(mm/dd/yyyy)");
		
		Scanner scanner = new Scanner(System.in);

		while (true) {
			String answer = scanner.nextLine();
			answer = answer.replace("\n", "").replace("\r", "");

			if (answer.equals("quit")) {
				System.exit(0);
			}

			Date date = new Date(answer);

			if (date.precedes(entity.getBorn())) {
				System.out.println("Incorrect. Try a later date.");
			} else if (entity.getBorn().precedes(date)) {
				System.out.println("Incorrect. Try an earlier date.");
			} else {
				Random random = new Random();
				int rd = random.nextInt(50);
				rd += 50; 
//				for(int i=0; i<=50*100; i++)
//					System.out.println("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n");
				System.out.println("*************Bingo!***************\n");
				System.out.printf("***Your bonus is %d$****\n", rd*100);
				break;
			}
		}
	}
	
	public void playGame() {
		while (true) {
			int entityId = genRandomEntityId();
			playGame(entityId);
		}
	}

	public int genRandomEntityId() {
		Random randomNumber = new Random();
		return randomNumber.nextInt(numOfEntities);
	}

	public static void main(String[] args) {
		System.out.println("=========================\n");
		System.out.println("     GuessMaster 1.0 \n");
		System.out.println("=========================");
		Politician jTrudeau = new Politician("Justin Trudeau", new Date("December", 25, 1971), 0.25, "Male", "Liberal");
		Singer cDion = new Singer("Celine Dion", new Date("March", 30, 1961), 0.5, "Female", "La voix du bon Dieu", new Date("November", 6, 1981));
		Country usa = new Country("United States", new Date("July", 4, 1776), 0.1, "Washington D.C.");

		GuessMaster gm = new GuessMaster();
		gm.addEntity(jTrudeau);
		gm.addEntity(cDion);
		gm.addEntity(usa);
		
		gm.playGame();
	}
}
