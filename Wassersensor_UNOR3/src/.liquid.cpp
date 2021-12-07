#include "U8glib.h" //Bibliothek für das Display
#include <Arduino.h>
U8GLIB_SH1106_128X64 u8g(U8G_I2C_OPT_NONE); //erzeugen des Display Objektes
void setup(void) {}
//Funktion zum zeichnen der Zeichenkette "Hello World!" 
//an der Position x=0 und y=20
void draw(void) {
  u8g.setFont(u8g_font_unifont);

  u8g.drawStr(0,30,"Philipp ist");

}
void loop(void) { 
  u8g.firstPage();  
  do {
    draw();
  } while( u8g.nextPage() );
  delay(100);
}