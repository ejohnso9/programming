;; file: annalyns_infiltration.clj
;;
;; AUTHOR: Erik Johnson
;; DATE: 2025Feb13
;;
;; DESCRIPTION
;;    https://exercism.org/tracks/clojure/exercises/annalyns-infiltration


(ns annalyns-infiltration)


;; test
(defn f [x] (+ f 2))

(defn can-fast-attack?
  "Returns true if a fast-attack can be made, false otherwise."
  [knight-awake?]
  (not knight-awake?)
)


(defn can-spy?
  "Returns true if the kidnappers can be spied upon, false otherwise."
  [knight-awake? archer-awake? prisoner-awake?]
  (or knight-awake? archer-awake? prisoner-awake?)
)


(defn can-signal-prisoner?
  "Returns true if the prisoner can be signalled, false otherwise."
  [archer-awake? prisoner-awake?]
  (and (not archer-awake?) prisoner-awake?)
)


(defn can-free-prisoner?
  "Returns true if prisoner can be freed, false otherwise."
  [knight archer prisoner dog]
  (or
    (and dog (not archer))
    (and (not dog) prisoner (not knight) (not archer))
  )
)

