//This script was used in the Stem World Education Services game Pizza One Two Three!.  It was used for the functionality of the check out button that
//would calculate the correctness of the toppings and the fraction when the player had made the pizza.  Rights are owned by Stem World Education Services.

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CheckOut : MonoBehaviour
{
    public static bool correctOrNot;	
    public static bool correctTopping;
    public float playerCut;
    public float gameCut;

    public void setWinConditions(){
        playerCut = Slice.cutChoicePortion * 30;
        gameCut = GameManager.answer[GameManager.orderIndex];
    }

    public bool CheckCorrectness()
    {

        
        if (Slice.cutChoicePortion * 30 == GameManager.answer[GameManager.orderIndex])
        {
            correctOrNot = true;
            return true;
        }
        else
        {
            correctOrNot = false;
            return false;
        }

    }

    public bool CheckToppingCorrectness(){
        bool correct = false;

        //RandomToppingDisplay Check
        if (RandomToppingDisplay.toppingtextvar == "Tomato Sauce" && ToppingCounter.tomato > 0 && ToppingCounter.pesto == 0){
            correct = true;
        }
        else if (RandomToppingDisplay.toppingtextvar == "Pesto" && ToppingCounter.pesto > 0 && ToppingCounter.tomato == 0){
            correct = true;
        }

        //RandomToppingE Check
        if (RandomToppingE.toppingtextvar2 == "Cheese" && ToppingCounter.cheese > 0 && ToppingCounter.olives == 0){
            correct = true;
        }
        else if (RandomToppingE.toppingtextvar2 == "Olives" && ToppingCounter.olives > 0 && ToppingCounter.cheese == 0){
            correct = true;
        }
        else if (RandomToppingDisplay.toppingtextvar == "Tomato Sauce" && RandomToppingE.toppingtextvar2 != "Olives" && RandomToppingE.toppingtextvar2 != "Cheese" && ToppingCounter.tomato > 0 && ToppingCounter.pesto == 0 && ToppingCounter.olives == 0 && ToppingCounter.cheese == 0){
            correct = true;
        }
        else correct = false;

        correctTopping = correct;
        return correct;
    }

    public void CheckOutMoney(float timeSpent)
	{
        Debug.Log("Here ---------------------------------------------------------------------------------------------");
		timeSpent = GameManager.timeNum;
		GameManager.thisRoundMon = 0;
        if (CheckCorrectness() == false && CheckToppingCorrectness() == false)
        {
            ToppingCounter.HintAdder = 4;
            GameManager.thisRoundMon += 0;
        }
        else if (CheckCorrectness() == false && CheckToppingCorrectness() == true)
        {
            ToppingCounter.HintAdder = 2;
            GameManager.thisRoundMon += 1;
        }
        else if (CheckCorrectness() == true && CheckToppingCorrectness() == false)
        {
            ToppingCounter.HintAdder = 3;
            if (timeSpent > 15)
            {
                GameManager.thisRoundMon += 8;
            }
            else if (timeSpent > 10)
            {
                GameManager.thisRoundMon += 15;
            }
            else if (timeSpent > 5)
            {
                GameManager.thisRoundMon += 40;
            }
            else if (timeSpent > 0)
            {
                GameManager.thisRoundMon += 50;
            }
        }
        else if (CheckCorrectness() == true && CheckToppingCorrectness() == true)
        {
            ToppingCounter.HintAdder = 1;
            if (timeSpent > 15)
            {
                GameManager.thisRoundMon += 15;
            }
            else if (timeSpent > 10)
            {
                GameManager.thisRoundMon += 30;
            }
            else if (timeSpent > 5)
            {
                GameManager.thisRoundMon += 80;
            }
            else if (timeSpent > 0)
            {
                GameManager.thisRoundMon += 100;
            }
        }
		GameManager.timeNum = 0;
	}
}
