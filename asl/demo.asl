/**
 * Demo BDI program
 * This example BDI program performs the action
 * 'do(action)' whenever it receives a perception 
 * of the format 'time(1234)'.
 * @author	Patrick Gavigan
 * @date	6 December 2019
 */

!demonstrate.

+!demonstrate
	:	time(A)
	<-	do(something);
		.broadcast(tell, heardTime(A));
		!demonstrate.
		
+!demonstrate
	<-	!demonstrate.
