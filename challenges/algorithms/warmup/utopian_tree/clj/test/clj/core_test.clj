(ns clj.core-test
  (:require [clojure.test :refer :all]
            [clj.core :refer :all]))

(deftest a-test
  (testing "1"
    (is (= (utopiantree 0) 1)))
  (testing "2"
    (is (= (utopiantree 1) 2)))
  (testing "9"
    (is (= (utopiantree 9) 62)))
  (testing "10"
    (is (= (utopiantree 10) 63)))
)
