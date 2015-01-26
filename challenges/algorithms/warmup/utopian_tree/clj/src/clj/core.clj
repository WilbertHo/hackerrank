(ns clj.core
  (:gen-class))

(defn utopiantree
  [end]
  (loop [n 0 acc 1]
    (if (= n end)
      acc
      (recur (inc n) (if (= (mod n 2) 1) (+ acc 1) (* acc 2)))
    )
  )
)

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (println (utopiantree 10)))
