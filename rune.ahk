#SingleInstance, force
Suspend, on

; Variables
thorn := true

; Toggle Script
!r:: Suspend, Toggle

; Runes
a::
    thorn := false
    Send, ᚪ
    Return

b::
    thorn := false
    Send, ᛒ
    Return

c::
    thorn := false
    Send, ᚳ
    Return

d::
    thorn := false
    Send, ᛞ
    Return

e::
    thorn := false
    Send, ᛖ
    Return

f::
    thorn := false
    Send, ᚠ
    Return

g::
    thorn := false
    Send, ᚷ
    Return

h::
    if (thorn) {
        Send, {BackSpace}
        Send, ᚦ    ; Thorn logic
    } else {
        Send, ᚻ
    }
    thorn := false
    Return

i::
    thorn := false
    Send, ᛁ
    Return

j::
    thorn := false
    Send, ᛡ
    Return

k::
    thorn := false
    Send, ᚴ    ; Medieval rune for "K"
    Return

l::
    thorn := false
    Send, ᛚ
    Return

m::
    thorn := false
    Send, ᛗ
    Return

n::
    thorn := false
    Send, ᚾ
    Return

o::
    thorn := false
    Send, ᚩ
    Return

p::
    thorn := false
    Send, ᛈ
    Return

q::
    thorn := false
    Send, ᛟ    ; Anglo-Saxon rune for "oe", used as a "q"
    Return

r::
    thorn := false
    Send, ᚱ
    Return

s::
    thorn := false
    Send, ᛋ
    Return

t:: 
    thorn := true
    Send, ᛏ
    Return


u::
    thorn := false
    Send, ᚢ
    Return

v::
    thorn := false
    Send, ᚡ    ; Medieval rune for "K"
    Return

w::
    thorn := false
    Send, ᚹ
    Return

x::
    thorn := false
    Send, ᛉ
    Return

y::
    thorn := false
    Send, ᚣ
    Return

z::
    thorn := false
    Send, ᛦ    ; Tolkien rune for "Z"
    Return


; Non-character keystrkoes
~Space::
    thorn := false
    Return

.::
    thorn := false
    Send, ᛫
    Return

~,::
    thorn := false
    Return

~BackSpace::
    thorn := false
    Return

~!::
    thorn := false
    Return

~?::
    thorn := false
    Return
