/* api1.c */

#include "api1.h"

/*@ requires fc_pre_API1_predicat1(a, b);
  @ assigns \nothing;
  @ ensures \result == a+b;
 */
int  API1_fonction1(int a, int b)
{
	return a + b;
}

/*@ requires fc_pre_API1_predicat2(a, b);
  @ assigns \nothing;
  @ ensures \result == a+b;
 */
int  API1_fonction2(int a, int b)
{
	return a + b;
}