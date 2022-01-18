#SingleInstance, force
Suspend, on

; Variables
state := 0

; Toggle Script
!r:: Suspend, Toggle

; Runes
a::
    state := 0
    Send, ᚪ
    Return

b::
    state := 0
    Send, ᛒ
    Return

c::
    state := 0
    Send, ᚳ
    Return

d::
    state := 0
    Send, ᛞ
    Return

e::
    state := 0
    Send, ᛖ
    Return

f::
    state := 0
    Send, ᚠ
    Return

g::
    if (state == 3) {
        Send, {BackSpace 2}
        Send, ᛝ
    } else {
        Send, ᚷ
    }
    state := 0
    Return

h::
    if (state == 1) {
        Send, {BackSpace}
        Send, ᚦ    ; Thorn logic
    } else {
        Send, ᚻ
    }
    state := 0
    Return

i::
    state := 2
    Send, ᛁ
    Return

j::
    state := 0
    Send, ᛡ
    Return

k::
    state := 0
    Send, ᚴ    ; Medieval rune for "K"
    Return

l::
    state := 0
    Send, ᛚ
    Return

m::
    state := 0
    Send, ᛗ
    Return

n::
    if (state == 2) {
        state := 3
    } else {
        state := 0
    }
    Send, ᚾ
    Return

o::
    state := 0
    Send, ᛟ
    Return

p::
    state := 0
    Send, ᛈ
    Return

q::
    state := 0
    Send, ᛩ    ; Stealing from medieval rune Q 
    Return

r::
    state := 0
    Send, ᚱ
    Return

s::
    state := 0
    Send, ᛋ
    Return

t:: 
    state := 1
    Send, ᛏ
    Return


u::
    state := 0
    Send, ᚢ
    Return

v::
    state := 0
    Send, ᚡ    ; Medieval rune for "K"
    Return

w::
    state := 0
    Send, ᚹ
    Return

x::
    state := 0
    Send, ᛉ
    Return

y::
    state := 0
    Send, ᚣ
    Return

z::
    state := 0
    Send, ᛣ    ; Tolkien rune for "Z"
    Return


; Non-character keystrkoes
~Space::
    state := 0
    Return

.::
    state := 0
    Send, ᛫
    Return

~,::
    state := 0
    Return

~BackSpace::
    state := 0
    Return

~!::
    state := 0
    Return

~?::
    state := 0
    Return
