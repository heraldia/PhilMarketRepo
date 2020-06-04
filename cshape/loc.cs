using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class loc : MonoBehaviour {

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
        print("旋转" + this.transform.localEulerAngles);

        print("X角度为：" + this.transform.localEulerAngles.x);

        print("位置坐标" + this.transform.localPosition);

        print("X坐标为：" + this.transform.localPosition.x);





    }
}
