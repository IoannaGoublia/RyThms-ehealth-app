Το σύστημα μας αποτελείται από δύο clients:
  1)e-health Tracker Device, το οποίο είναι ο simulator του wearable μέσα στο οποίο θα βρίσκονται οι αισθητήρες μας
  2)e-health Tracker Web app, το οποίο αποτελεί την εφαρμογή του χρήστη
Ο κεντρικός server του συστήματος χωρίζεται σε δυο μέρη τα οποία βρίσκονται στον ίδιο υπολογιστή:
  1)Ένας server γραμμένος σε python, ο οποίος λαμβάνει τις τιμές από το e-health Tracker Device και τις αποθηκεύει στη βάση δεδομένων(MS SQL SERVER)
  2)Ο web server γραμμένος σε nodejs, ο οποίος διαχειρίζεται τα requests του e-health Tracker Web app, επικοινωνώντας με τη βάση δεδομένων(MS SQL SERVER)
Η λογική των δύο τμημάτων server εξυπηρετεί τη λογική, σε περίπτωση που πάθει κάτι ο webserver, να μην χάνονται τα δεδομένα που στέλνει το device.

Αρκεί να έχουμε κατεβάσει μία έκδοση της python από την 3.8 και μετά(για να είναι αναβαθμισμένο το pip), και την nodejs

Στην A version το σύστημα μας τρέχει στο localhost.
Για να μπορέσουμε να τρέξουμε την εφαρμογή ακολουθούμε τα παρακάτω βήματα:
 1)Τρέχουμε τον e-healthTrackerDeviceserver.py στο cmd 
 2)Τρέχουμε το  e-healthTrackerDeviceclient.py στο idle της python
 3)Στο cmd σε νέο παράθυρο πηγαίνοντας στο directory- "C:/Users/User/Desktop/myproject/nodeapp" τρέχουμε τον web server πατώντας npm start (το myproject αρχείο περιλαμβάνει 
το αρχείο nodeapp, μεσά στο οποία υπάρχει η δομή MVC του server, ex routes, views, public, database)
 4)Ανοίγωντας έναν οποιοδήποτε browser, και πληκτρολογώντας στο url -localhost:3000 μας εμφανίζεται η αρχική σελίδα welcome και στη συνέχεια ανάλογα με τις ενέργειες 
που θα ακολουθήσουμε, πλοηγούμαστε την εφαρμογή