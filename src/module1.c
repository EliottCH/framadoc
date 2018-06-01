/* module1.c */

#include "module1.h"

/*@ requires fc_pre_module1_predicat1(a, b);
  @ assigns \nothing;
  @ ensures \result == a+b;
 */

int  module1_fonction1(int a, int b)
{
	return a + b;
}

/*@ requires fc_pre_module1_predicat2(a, b);
  @ assigns \nothing;
  @ ensures \result == a+b;
 */
int  module1_fonction2(int a, int b)
{
	return a + b;
}