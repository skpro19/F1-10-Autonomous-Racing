
(cl:in-package :asdf)

(defsystem "autoturtle-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "AddTwoInts" :depends-on ("_package_AddTwoInts"))
    (:file "_package_AddTwoInts" :depends-on ("_package"))
    (:file "TeleportTurtle" :depends-on ("_package_TeleportTurtle"))
    (:file "_package_TeleportTurtle" :depends-on ("_package"))
  ))