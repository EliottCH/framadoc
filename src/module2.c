/* module2.c */

#include "module2.h"

/*@ requires fc_pre_module2_predicat1(a, b);
  @ assigns \nothing;
  @ ensures \result == a+b;
 */
int  module2_fonction1(int a, int b)
{
	return a + b;
}

/*@ requires fc_pre_module2_predicat2(a, b);
  @ assigns \nothing;
  @ ensures \result == a+b;
 */
int  module2_fonction2(int a, int b)
{
	return a + b;
}