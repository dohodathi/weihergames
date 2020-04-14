# Grundregeln

## Fundamentale Regeln

Diese gelten für alles im Zusammenhang mit den Weihergames.

   **§ 1.**  Jeder Stein/Ball der aus der Hand fällt während der Runde wird ungültig.

   **§ 2.**  Ein ungültiger Zug/Wurf/Aktion wird als ungültig gewertet. Dabei sollte beachtet werden, dass der *Worst-Case* angenommen wird. Im Zweifel wird die Runde gegen den Spieler gewertet.

   **§ 3.**  Ist nicht geregelt welcher Spieler anfängt/etc wird dies per Zufall entschieden.

---

## Standard-Punkte-Regel (SPR)

Wenn ein Spiel es nicht anders definiert, unterliegt das Spiel der **SPR**. Ein Spiel kann ebenso auf der SPR aufbauen und jene Regeln mit Zusätzen erweitern.

Die SPR schreibt folgende Regeln vor:
**§ 1.**  Ein Spiel hat X Sätze, jeder Satz hat `Y = Math.ceiling(30/playerscount)` Punkte.
**§ 2.**  Ein Spieler gewinnt den Satz, sobald er mindestens 2 Punkte Vorsprung vor allen Mitspielern hat.
**§ 3.**  Jeder Spieler darf seine Zug ausspielen, auch wenn ein Spieler in der selben Runde die Zielpunktzahl erreicht hat.
**§ 4.**  Es wird immer minimal ein Satz mit minimal `Y = Math.ceiling(30/playerscount)` Punkten gespielt.

## Anforderung an die Spieler
Die Spieler müssen vor dem Spiel festlegen, wieviele Sätze gespielt werden. Je nach Anzahl Spieler empfhielt sich ein Best-of-X System, oder ein Punkte System je nach Platzierung im Satz.

---

## Season Rules / Turnier-Regeln

Jedes Spiel welches in einem Turnier aufgenommen wird, muss bis zu 5 Spieler unterstützen. Das bedeutet, es müssen für jedes Spiel sinnvolle Regeln für bis zu 5 Spieler bestehen, bevor das Spiel in einem Turnier gespielt werden kann.

### 2 Spieler
*Schlag-den-Raab* Punkteregel (Punktzahl korreliert mit Spielnummer, zB erstes Spiel 1Punkt, fünftes Spiel 5Punkte).

### Mehr als 2 Spieler
Es gilt die 3-1-Punkt-Regel. Der erste Platz erhält 3 Punkte, der zweite Platz erhält 1 Punkt. Die anderen Spieler erhalten keine Punkte.

### Mehr als 5 Spieler
Für jedes Spiel werden Gruppen mit maximal 5 Spielern gebildet. Dabei gilt das Zufallsprinzip zur Zuordnung der Spieler auf die Gruppen.
Die Gruppe spielen das Spiel nach der 3-1-Punkt-Regel.
