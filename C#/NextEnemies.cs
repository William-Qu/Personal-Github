//This script was used in the Stem World Education Services game Math Towers.  It was used for the functionality of the next enemy display which shows
//which enemies are to spawn next.  Rights are owned by Stem World Education Services.

using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NextEnemies : MonoBehaviour
{
    public int levelNumber;
    public GameObject textbox;
    public GameObject enemySpawner;
    public int[] NextNumberList;
    public static int enemiesLeftInWave;
    public string printList;

    private GameObject Anchor;

    // Start is called before the first frame update
    void Start()
    {
        enemiesLeftInWave = 5;
        NextNumberList = new int[5];
    }

    // Update is called once per frame
    void Update()
    {
        UpdateNumberList();
        StringifyList();
        textbox.GetComponent<TMPro.TextMeshProUGUI>().text = printList;
    }

    public void setAnchors(bool active){
        for (int i = 4; i <= 6; i++){
            Anchor = GameObject.Find("Anchor: (" + levelNumber.ToString() + ", " + i.ToString() + ")");
            Anchor.GetComponent<Tower>().inactiveAnchor = active;
        }
    }

    public void UpdateNumberList(){
        int startNewWave = 0;

        if (enemySpawner.GetComponent<EnemySpawner>().enemyList[0] == 0){
            enemiesLeftInWave = 5;
            startNewWave = 1;
        }

        if (enemySpawner.GetComponent<EnemySpawner>().enemyList.Count < enemiesLeftInWave + startNewWave){
            enemiesLeftInWave = enemySpawner.GetComponent<EnemySpawner>().enemyList.Count;
        }

        for (int i = startNewWave; i < enemiesLeftInWave + startNewWave; i++){
            if (enemySpawner.GetComponent<EnemySpawner>().enemyList[i] == 0){
                enemiesLeftInWave = i - startNewWave;
                break;
            }

            NextNumberList[i - startNewWave] = enemySpawner.GetComponent<EnemySpawner>().enemyList[i];
        }
    }

    public void StringifyList(){
        printList = "";

        for (int i = 0; i < enemiesLeftInWave-1; i++){
            printList = printList + NextNumberList[i].ToString() + ", ";
        }
        printList = printList + NextNumberList[enemiesLeftInWave-1].ToString();
    }
}
