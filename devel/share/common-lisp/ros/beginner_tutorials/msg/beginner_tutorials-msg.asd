
(cl:in-package :asdf)

(defsystem "beginner_tutorials-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Num" :depends-on ("_package_Num"))
    (:file "_package_Num" :depends-on ("_package"))
    (:file "anglesMsg" :depends-on ("_package_anglesMsg"))
    (:file "_package_anglesMsg" :depends-on ("_package"))
    (:file "encodersFeedback" :depends-on ("_package_encodersFeedback"))
    (:file "_package_encodersFeedback" :depends-on ("_package"))
    (:file "speedMsg" :depends-on ("_package_speedMsg"))
    (:file "_package_speedMsg" :depends-on ("_package"))
  ))