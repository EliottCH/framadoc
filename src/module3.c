/* module3.c */

#include "module3.h"

/*@ requires fc_pre_module3_predicat1(a, b);
  @ assigns \nothing;
  @ ensures \result == a+b;
 */
int  module3_fonction1(int a, int b)
{
	return a + b;
}

/*@ requires fc_pre_module3_predicat2(a, b);
  @ assigns \nothing;
  @ ensures \result == a+b;
 */
int  module3_fonction2(int a, int b)
{
	return a + b;
}