# Tutorial sources and naming conventions

The examples retained in [Mainframe/ZOS](Mainframe/ZOS) use the naming
conventions below to identify their original tutorials. This repository now
tracks only the z/OS implementation and its supporting files.


['Beginning COBOL for Programmers' by Michael Coughlan](http://www.apress.com/9781430262534) :

My Source: BDS0X0Y

Where 0X is the chapter number and 0Y is the exercise number.

For example: Listing8-1.cbl becomes:

BDS0801.cbl


[The Open Mainframe Project](https://www.openmainframeproject.org/projects/coboltrainingcourse) :

My Source : ODSXXXX

Where XXXX is as close as I can match with the original name.

For example: CBL0001.cobol becomes:

ODS0001.cbl


[Enterprise COBOL For Business Application Programming](https://community.ibm.com/community/user/ibmz-and-linuxone/viewdocument/enterprise-cobol-for-business-appli?CommunityKey=b0dae4a8-74eb-44ac-86c7-90f3cd32909a&tab=librarydocuments)

This tutorial is more encompassing than the other tutorials so it makes for a difficult workflow/renaming strategy.

It seems the easiest way forward is to create a new member for each workshop.

My Source: WSXXX

Where XXX is the Workshop number. For example, Workshop 5.3.2 is
[WS532.cbl](Mainframe/ZOS/ECBAP/cbl/WS532.cbl).

A lot of the Workshops are modifying existing programs so the new member will just be that but in SCM to be able to restore the code if need be.

The FAV series of programs are created using my prefered structure, naming conventions etc. This includes FAVRPT and FAVRFP.

But, in any case, they will always be identified by the Workshop number.

The assignments and their historical status are listed in
[README4](README4.md). See [README3](README3.md) for the retained z/OS examples;
the assignment history is not a list of files included in this repository.

Hey, where did the other code go?
It wasn't my code. I didn't have explicit permission to post it so it was removed.
