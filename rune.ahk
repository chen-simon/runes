#SingleInstance, force
Suspend, on

; State
state := ""

; Toggle Script
!r:: Suspend, Toggle

; Runes
a::
    state := ""
    Send, ᚫ
    Return

b::
    state := ""
    Send, ᛒ
    Return

c::
    state := ""
    Send, ᚳ
    Return

d::
    state := ""
    Send, ᛞ
    Return

e::
    state := ""
    Send, ᛖ
    Return

f::
    state := ""
    Send, ᚠ
    Return

g::
    if (state == "in") {
        state := ""
        Send, {BackSpace 2}
        Send, ᛝ
    } else if (state == "ou") {
        state := "oug" 
        Send, ᚷ
   } else {
        state := ""
        Send, ᚷ
    }
    Return

h::
    if (state == "t") {
        state := ""
        Send, {BackSpace}
        Send, ᚦ
    } else if (state == "oug") {
        state := ""
        Send {BackSpace 3}
        Send, ᛟ
    } else {
        state := ""
        Send, ᚻ
    }
    Return

i::
    state := "i"
    Send, ᛁ
    Return

j::
    state := ""
    Send, ᛡ
    Return

k::
    state := ""
    Send, ᚴ    ; Medieval rune for "K"
    Return

l::
    state := ""
    Send, ᛚ
    Return

m::
    state := ""
    Send, ᛗ
    Return

n::
    if (state == "i") {
        state := "in"
    } else {
        state := ""
    }
    Send, ᚾ
    Return

o::
    state := "o"
    Send, ᚩ
    Return

p::
    state := ""
    Send, ᛈ
    Return

q::
    state := ""
    Send, ᛩ    ; Stealing from medieval rune Q 
    Return

r::
    state := ""
    Send, ᚱ
    Return

s::
    state := ""
    Send, ᛋ
    Return

t:: 
    state := "t"
    Send, ᛏ
    Return


u::
    if (state == "o") {
        state := "ou"
    } else {
        state := ""
    }
    Send, ᚢ
    Return

v::
    state := ""
    Send, ᚡ    ; Medieval rune for "K"
    Return

w::
    state := ""
    Send, ᚹ
    Return

x::
    state := ""
    Send, ᛉ
    Return

y::
    state := ""
    Send, ᚣ
    Return

z::
    state := ""
    Send, ᛣ    ; Tolkien rune for "Z"
    Return


; Non-character keystrkoes
~Space::
    state := ""
    Return

.::
    state := ""
    Send, ᛫
    Return

~,::
    state := ""
    Return

~BackSpace::
    state := ""
    Return

~!::
    state := ""
    Return

~?::
    state := ""
    Return

~Enter::
    state := ""
    Return
