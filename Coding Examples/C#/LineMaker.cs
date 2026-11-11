using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;

/*
This Unity file was developed by William Quigley for Stem World Educational Services as a testing ground for an object cutting function for the game "Pizza
One Two Three!".  The feature was going to be used determine the fraction that the player would have created with their cuts, but was later changed to a 
different feature for ease of use purposes.

During the runtime of the Unity program, a player can cut the circle into multiple pieces by clicking on two spots around the edges of the
circle, and the line will cut the circle accordingly.  This is done by not actually cutting the circle, but instead by duplication the object and using
object specific sprite masks to hide the sections of the circle.  This way, when a 'cut' is made, the circle will be duplicated, and the right side of the 
first circle will be covered, and the left side of the second circle will be covered, making it appear as if the shape has been cut in two.  This is then 
done recursively to allow for multiple cuts to overlap.

This class will "cut" a sprite in two.  To do this the sprite must follow a special format in the Unity Editor; it must be the child of an empty object 
that has the component "SortingGroup".  This empty object must have another child that is a sprite mask (must be the second child in the list) with a
10x10 scale.  The sprite must also be a 2D rigid body, and have some sort of collider with "IsTrigger" enabled.  The object this class will be apart of 
must also be an empty object and must have a mesh renderer, a mesh filter, an edge collider, a 2D rigid body, and this class.  Make sure to set 
gravity in the rigid body to zero, the original edge collider points to (0,0), and a material to mat in this script, then this code will be usable.

All rights to this program is owned by Stem World Educational Services.
*/

public class LineMaker : MonoBehaviour
{
    public Vector3 PointA;
    public Vector3 PointB;
    public int sliceCount = 10;
    public Material mat;

    private bool pointMake;
    private double Theta;
    private int numCuts;
    private bool cutCount;


    void Update(){
        //Get the position of the mouse and map it to the cameras' coordinate system
        Vector3 mousePos = Input.mousePosition;
        Vector3 objPos = Camera.main.ScreenToWorldPoint(mousePos);

        //If the mouse is pressed down then gather a point in A or B depending on which one was last gathered
        if (Input.GetButtonDown("Fire1") && pointMake == false){
            PointA.Set(objPos.x, objPos.y, 0f);
            pointMake = true;
        }
        else if (pointMake && Input.GetButtonDown("Fire1")){
            PointB.Set(objPos.x, objPos.y, 0f);
            Vector3[] vertices = pointPlotter();
            DrawRect(vertices);
            pointMake = false;
            ColliderDefiner(PointA.x, PointA.y, PointB.x, PointB.y);
            if (cutCount == true){
                numCuts++;
                cutCount = false;
            }
        }
    }

    //This is a built in function that is called when a collision is detected between two objects
    private void OnTriggerEnter2D(Collider2D col){
        Debug.Log("Hit");
        //Gets the empty object parent and cuts the circle
        Transform emptyObj = col.transform.parent;
        cut(emptyObj);

        //Resets the collider so that it can collide with the same object twice in a row
        cutCount = true;
        ColliderDefiner(0f, 0f, 0f, 0f);
    }

    //Set the two points on the edge collider to be points A and B so the collider moves with the generated lines
    private void ColliderDefiner(float Ax, float Ay, float Bx, float By){
        List<Vector2> edgeList = new List<Vector2>();
        edgeList.Add(new Vector2(Ax, Ay));
        edgeList.Add(new Vector2(Bx, By));
        bool pointSet = GetComponent<EdgeCollider2D>().SetPoints(edgeList);
    }

    //This will be called once a collision has already occurred to cut the sprite into two pieces
    public void cut(Transform emptyObj){
        Transform emptyObjOne = Instantiate(emptyObj, emptyObj.position, emptyObj.rotation);
        Transform emptyObjTwo = Instantiate(emptyObj, emptyObj.position, emptyObj.rotation);

        //Set the cloned empty GameObjects as children of the parent Empty Object
        emptyObjOne.SetParent(emptyObj);
        emptyObjTwo.SetParent(emptyObj);

        //Defines the copied masks and circles for later refrence
        Transform baseCircOne = emptyObjOne.GetChild(0);
        Transform baseCircTwo = emptyObjTwo.GetChild(0);

        Transform baseMaskOne = Instantiate(emptyObjOne.GetChild(1), emptyObj.position, emptyObj.rotation);
        Transform baseMaskTwo = Instantiate(emptyObjTwo.GetChild(1), emptyObj.position, emptyObj.rotation);
        
        if (numCuts == 0){
            Destroy(emptyObj.GetChild(1).gameObject);
            Destroy(emptyObjOne.GetChild(1).gameObject);
            Destroy(emptyObjTwo.GetChild(1).gameObject);
        }

        baseMaskOne.SetParent(emptyObjOne);
        baseMaskTwo.SetParent(emptyObjTwo);

        //Sets the copied circles at the position and rotation of the parent Empty Object, which is the orientation of the parent circles
        baseCircOne.position = emptyObj.position;
        baseCircTwo.position = emptyObj.position;
        baseCircOne.rotation = emptyObj.rotation;
        baseCircOne.rotation = emptyObj.rotation;

        //Calculates the midpoints of the x and y values of the lines
        float Midx = (PointA.x + PointB.x) / 2;
        float Midy = (PointA.y + PointB.y) / 2;

        //Sets the positions and rotations of the copied masks 
        baseMaskOne.rotation = Quaternion.Euler(0f, 0f, Convert.ToSingle(Theta * 180 / Mathf.PI));
        baseMaskTwo.rotation = Quaternion.Euler(0f, 0f, Convert.ToSingle(Theta * 180 / Mathf.PI));
        baseMaskOne.position = new Vector3(Convert.ToSingle(Midx - 4.9f * Math.Sin(Theta)), Convert.ToSingle(Midy+ 4.9f * Math.Cos(Theta)), 0f);
        baseMaskTwo.position = new Vector3(Convert.ToSingle(Midx + 4.9f * Math.Sin(Theta)), Convert.ToSingle(Midy- 4.9f * Math.Cos(Theta)), 0f);

        //Deletes the parent circle and the parent mask
        Destroy(emptyObj.GetChild(0).gameObject);
        if (numCuts != 0){
            for (int i = 1; i <= numCuts; i++)
                Destroy(emptyObj.GetChild(i).gameObject);
        }   

        CleanUseless(emptyObjOne);
        CleanUseless(emptyObjTwo);
        sliceCount++;
    }

    private void CleanUseless(Transform emptyObj){
        float aveX = 0f;
        float aveY = 0f;
        int maskNum = 0;

        //Totals the x and y positions of the masks
        for (int k = 1; k <= numCuts+1; k++){
            //Debug.Log("x is " + emptyObj.GetChild(k).position.x + " and y is "+ emptyObj.GetChild(k).position.y);
            aveX += emptyObj.GetChild(k).position.x;
            aveY += emptyObj.GetChild(k).position.y;
            maskNum++;
        }

        //Finds the average of the x and y 
        aveX = aveX / maskNum;
        aveY = aveY / maskNum;
        //Debug.Log("maskNum is " + maskNum);

        //Checks to make sure that the average is within the required limit, and if so, then destroy the object
        //Debug.Log("aveX is " + aveX + ", aveY is " + aveY);
        if (aveX <= emptyObj.position.x + 2.25f &&
            aveX >= emptyObj.position.x - 2.25f &&
            aveY <= emptyObj.position.y + 2.25f &&
            aveY >= emptyObj.position.y - 2.25f){
            //If the average is in the middle (within range), then check that all of the masks cover the midpoint.  If they do, then this must be deleted
            if (checkMiddle(emptyObj)){
                Destroy(emptyObj.gameObject);
                Debug.Log("Tanked------------------------------------------------------------------------------------------");
                sliceCount--;
            }
            else{
                Debug.Log("Close but no cigar******************************************************************************");
                //areaCollector(emptyObj);
            }
        }
        else{
            Debug.Log("All good here");
            //areaCollector(emptyObj);
        }
    }

    private bool checkMiddle(Transform emptyObj){
        bool CoverMid = true;

        //If any of the masks doesn't cover the midpoint, then we're good
        for (int i = 1; i <= numCuts+1; i++){
            //Sets up a bounding box to the masks position
            Bounds mask = new Bounds();
            mask.center = emptyObj.GetChild(i).position;
            mask.extents = new Vector3(5.5f, 5.5f, 0f);

            //Sets a point to the emptyObjs position
            Vector3 midpoint = new Vector3(emptyObj.position.x, emptyObj.position.y, 0f);

            //Checks whether the point is contained in the bounding box
            if (mask.Contains(midpoint) == false){
                CoverMid = false;
            }
        }
        return CoverMid;
    }

    /*
    private void areaCollector(Transform emptyObj){
        int numPoints = 0;
        int numInside = 0;
        int numMasks = 0;
        float area = 0f;

        for (float i = emptyObj.position.x - 2.5f; i <= emptyObj.position.x + 2.5f; i += 0.1f){
            for (float j = emptyObj.position.y - 2.5f; i <= emptyObj.position.y + 2.5f; i += 0.1f){
                for (int k = 1; k <= numCuts + 1; k++){
                    GameObject maskRot = new GameObject();
                    maskRot.transform.position = emptyObj.GetChild(k).position;

                    GameObject pointRot = new GameObject();
                    pointRot.transform.position = emptyObj.position;

                    maskRot.transform.RotateAround(maskRot.transform.position, emptyObj.position, -1 * emptyObj.GetChild(k).eulerAngles.z);
                    pointRot.transform.RotateAround(pointRot.transform.position, emptyObj.position, -1 * emptyObj.GetChild(k).eulerAngles.z);

                    Vector3 point = new Vector3(pointRot.transform.position.x, pointRot.transform.position.y, 0f);
                    
                    Bounds mask = new Bounds();
                    mask.center = maskRot.transform.position;
                    mask.extents = new Vector3(5f, 5f, 0f);

                    if (mask.Contains(point)){
                        numInside++;
                    }
                    numMasks++;

                    Destroy(pointRot);
                    Destroy(maskRot);
                }

                if (numInside != numMasks) {
                    numPoints++;
                }

                numInside = 0;
                numMasks = 0;
            }
        }

        area = numPoints * 0.01f;
        emptyObj.tag = area.ToString();
    }
    */

/*  
    private void CleanUseless(Transform emptyObj){
        //Usable variables
        bool fullyCovered = true;
        int notCovered = 0;
        float angle = 0f;

        //These first two for loops are to tile with the x and the y points
        for (float i = emptyObj.position.x-2.5f; i <= emptyObj.position.x+2.5f; i+=0.1f){
            for (float j = emptyObj.position.y-2.5f; j <= emptyObj.position.y+2.5f; j+=0.1f){
                //Go through all of the masks and check to see if they all cover the point
                for (int k = 1; k <= numCuts+1; k++){
                    //Make a new game object for the point
                    GameObject point = new GameObject();
                    Bounds mask = new Bounds();

                    //Set mask and point
                    point.transform.position = new Vector3(i, j, 0f);
                    angle = emptyObj.GetChild(k).eulerAngles.z;

                    mask.center = emptyObj.GetChild(k).position;
                    mask.extents = new Vector3(5f, 5f, 0f);

                    //Rotate point around mask and set masks rotation
                    point.transform.RotateAround(point.transform.position, mask.center, -1 * angle);

                    //Check if the point is not covered, and if so add one to notCovered
                    //if (point.transform.position.x >= mask.transform.position.x+5f && point.transform.position.x <= mask.transform.position.x-5f && point.transform.position.y <= mask.transform.position.y+5f && point.transform.position.y >= mask.transform.position.y-5f){
                    
                    if(mask.SqrDistance(point.transform.position) >= 100 ){
                        notCovered++;
                    }
                  
                    //Debug.Log(mask.SqrDistance(point.transform.position));
                    //Reset the angle of the mask
                    //mask.transform.RotateAround(mask.position, emptyObj.position, angle);
                    Destroy(point);
                    //Destroy(mask);
                }
                if (notCovered == numCuts){
                    fullyCovered = false;
                }
                
                //Reset notCovered and point for next loop
                notCovered = 0;
            }
        }

        //Check whether or not the circle is fully covered
        if (fullyCovered == false){
            Debug.Log("All good here chief");
        }
        if (fullyCovered == true){
            Debug.Log("Destroyed");
            Destroy(emptyObj.gameObject);
        }
    }  
 */
 /*
    private void CleanUseless(Transform emptyObj){
        bool fullyCovered = true;
        int notCovered = 0;
        int runs = 0;
        float angle = 0f;

        for (float i = (emptyObj.position.x - 2.5f); i <= (emptyObj.position.x + 2.5f); i += 0.1f){
            for (float j = (emptyObj.position.y - 2.5f); j <= (emptyObj.position.y + 2.5f); j += 0.1f){
                for (int k = 1; k <= numCuts + 1; k++){
                    GameObject point = new GameObject();
                    point.transform.position = new Vector3(i, j, 0f);
                    Transform Tpoint = emptyObj.GetChild(k);
                    angle = Tpoint.transform.eulerAngles.z;

                    point.transform.RotateAround(Tpoint.transform.position, Vector3.forward, Tpoint.transform.eulerAngles.z * -1f);
                    Tpoint.eulerAngles = new Vector3(0f, 0f, 0f);

                    if (point.transform.position.x <= (Tpoint.transform.position.x + 5f) && point.transform.position.x >= (Tpoint.transform.position.x - 5f) && point.transform.position.y <= (Tpoint.transform.position.y + 5f) && point.transform.position.y >= (Tpoint.transform.position.y - 5f)){}
                    else{
                        notCovered++;
                    }
                    runs++;
                    //Debug.Log(runs);
                    Tpoint.eulerAngles = new Vector3(0f, 0f, angle);
                    Destroy(point);
                }
                if (notCovered == runs && notCovered != 0) {
                    fullyCovered = false;
                    break;
                }
                notCovered = 0;
                runs = 0;
            }
            if (fullyCovered == false) break;
        }
        if (fullyCovered == false){
            Debug.Log("Destroyed");
            Destroy(emptyObj.gameObject);
        }
    }
    */
    
    /*
    private bool Contains(Rect rect, float rectAngle, Point point){
    // rotate around rectangle center by -rectAngle
    var s = Math.Sin(-rectAngle);
    var c = Math.Cos(-rectAngle);

    // set origin to rect center
    var newPoint = point - rect.center;
    // rotate
    newPoint = new Point(newPoint.x * c - newPoint.y * s, newPoint.x * s + newPoint.y * c);
    // put origin back
    newPoint = newPoint + rect.center;

    // check if our transformed point is in the rectangle, which is no longer
    // rotated relative to the point

    return newPoint.x >= rect.xMin && newPoint.x <= rect.xMax && newPoint.y >= rect.yMin && newPoint.y <= rect.yMax;
}

Tpoint.transform.position = point;
                        Tpoint.transform.rotation = emptyObj.rotation;
                        //Tpoint.transform.SetParent(emptyObj.GetChild(k));
                        point = Tpoint.transform.position - emptyObj.GetChild(k).transform.position;
                        length = Mathf.Sqrt(Mathf.Pow(point.x, 2f) + Mathf.Pow(point.y, 2f));
                        if (length <= 8.2f){}    
*/

    //Draws a line between the selected points to the screen
    private void DrawRect(Vector3[] vertices){
        //Make the new mesh
        Mesh mesh = new Mesh();

        //Get the points of the rectangle
        vertices = pointPlotter();

        //Add these points to a Vector3 list of the vertices, and to a triangles list for them to be generated
        mesh.vertices = vertices;
        mesh.triangles = new int[] {0, 1, 2, 1, 2, 3};

        //Set the materials of the drawn lines
        GetComponent<MeshRenderer>().material = mat;
        GetComponent<MeshFilter>().mesh = mesh;
    }
        
    //Makes a list of the vertices based on Point A and Point B for the mesh to draw triangles onto
    private Vector3[] pointPlotter(){
        //Necessary calculations to find the locations of the lines
        float DeltaX = PointB.x - PointA.x;
        float DeltaY = PointB.y - PointA.y;
        Theta = Math.Atan(DeltaY/DeltaX);

        //If Theta is negative it changes Theta into a positive to preserve calculations
        if (Theta < 0) 
            Theta += (2 * Mathf.PI);

        //Create the Vector3 vertices list
        Vector3[] vertices = new Vector3[4];
        
       //Create the points
        vertices[0] = new Vector3(Convert.ToSingle(PointB.x + 0.1*Math.Sin(Theta)),  Convert.ToSingle(PointB.y - 0.1*Math.Cos(Theta)), 0f);
        vertices[1] = new Vector3(Convert.ToSingle(PointB.x - 0.1*Math.Sin(Theta)),  Convert.ToSingle(PointB.y + 0.1*Math.Cos(Theta)), 0f);
        vertices[2] = new Vector3(vertices[0].x - DeltaX,                            vertices[0].y - DeltaY, 0f);
        vertices[3] = new Vector3(vertices[1].x - DeltaX,                            vertices[1].y - DeltaY, 0f);

        return vertices;
    }
}