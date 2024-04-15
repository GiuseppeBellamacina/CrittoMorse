# CrittoMorse

Prova iniziale sull'algoritmo crittografico basato sul codice Morse.

L'algoritmo in questione traduce inizialmente un testo o un file in codice Morse, successivamente cambia i puntini in 0 e i trattini in valori numerici random. Il codice viene poi invertito.

A questo punto il codice si può epurare dagli spazi e dagli '/' di separazione delle parole, e si crea una chiave che servirà da mappa per riformattare nuovamente il testo crittato.

Essenzialmente si creano 2 stringhe, una chiamata testo criptato e l'altra chiave, che però sono una il testo criptato o la chiave dell'altra. Quindi non è possibile decriptarne una senza avere l'altra.
