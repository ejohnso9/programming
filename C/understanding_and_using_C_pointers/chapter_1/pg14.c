#include <stdio.h>

// 2025Mar24 ej
// page 14 of "Understanding and Using C Pointers"
// states that two void* pointers will never be equal to each other
// (and then immediately breaks this declaration by stating that that
// doesn't hold when they are both assigned to NULL).
//
// Q: Does that prove to be true using gcc @pythonanywhere?
// A: No, the claim does not hold. This program has two void* pointers
//    set to address of same int, both compare equal! Even a void*
//    pointer copared to an int* pointer can compare equal!
//
//    The text does state "The actual behavior of void pointers is system dependent."
//    INDEED: as verified here, it depends on your system, and C is
//    generally not as portable as one might think.
//
//    MORAL: You'd better verify correct behavior for your "system" -
//    that could mean update to OS version is really a different system,
//    update to compiler is really a different "system". A robust unit
//    test suite will go a long ways toward quickly verifying correct
//    behavior of a system (unfortunately, often viewed as a "luxury"
//    development teams can't afford. Can you afford unknown
//    misbehaviors? (i.e., wrong answers you are not aware are wrong?)

int main () {
    int a = 17;
    int b = 19;
    int i = 42;

    int* ap = &a;
    int* bp = &b;
    int* ip = &i;

    void* vp_1 = &a;  // no different when assigning 'ap'
    void* vp_2 = &a;  // I do mean 'a', here.

    // dump what we know
    printf("a is: %d\n", a);
    printf("b is: %d\n", b);
    printf("i is: %d\n", i);
    printf("\n");

    printf("ap is: %p\n", ap);
    printf("bp is: %p\n", bp);
    printf("ip is: %p\n", ip);
    printf("\n");

    printf("vp_1 is: %p\n", vp_1);
    printf("vp_2 is: %p\n", vp_2);
    printf("\n");

    // vp_1 and vp_2 equal?
    if (vp_1 == vp_2)
        printf("A: vp_1 == vp_2\n");
    else
        printf("A: vp_1 != vp_2\n");

    // what about vp_1 and ap: they are both set to address of 'a'
    if (vp_1 == ap)  
        printf("B: vp_1 == ap FALSE: A pointer to void will never be equal to another pointer.\n");
    else
        printf("B: vp_1 != ap\n");

    // Now are they equal?
    vp_1 = NULL;
    vp_2 = NULL;
    printf("after NULL set, vp_1 is: %p\n", vp_1);
    printf("after NULL set, vp_2 is: %p\n", vp_2);
    if (vp_1 == vp_2)
        printf("C: vp_1 == vp_2\n");
    else
        printf("C: vp_1 != vp_2\n");

    printf("\n");
    return(0); // NORMAL EXIT
}

// EOF

