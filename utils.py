import re
import nltk
import string
import spacy
from nltk.corpus import stopwords

STOPWORDS = set(stopwords.words("english"))


def remove_stopwords(text):
    """custom function to remove the stopwords"""
    return " ".join([word for word in str(text).split() if word not in STOPWORDS])


PUNCT_TO_REMOVE = string.punctuation


def remove_punctuation(text):
    """custom function to remove the punctuation"""
    return text.translate(str.maketrans("", "", PUNCT_TO_REMOVE))


def get_processed_transcript(url):
    # add necessary block to get the transcript
    text = """something that's always bugged me is how
hard it is to dunk a ball it's so high I

took my inability to dunk personally so
I decided to engineer some
UPS these are dunk Boots imagine a dunk
so high you have to be on a rope or
you'll break your
legs you know what you don't have to
imagine it because that's what we're
doing
well after we work out the
Kinks these are really similar to
inspector gadgets boots do you remember
go go gadget boots and that was
basically my mission statement for this
project extendable stilts on command
that could make me Ascend into the
heavens and that ideally I could take a
step with which I technically I think
satisfied that last part I also wasn't
satisfied with a standard dunk that's 10
ft the world record is 12 ft but I
designed these to go up to 16 ft I
really don't know why I guess I have a
thing for absurd basketball

stuff although in retrospect I should
have stopped at regulation height trying
to go as high as I possibly can made
things exponentially more complicated
and it's also really

dangerous my initial idea was some kind
of scissor mechanism like you'd see on
one of these lifts it has a bunch of
linkages that kind of expand like an
accordion when it's pushed by this
hydraulic ram and I can even do a record
setting dunk in
this unfortunately this lift weighs
about 3,000 lb so I can attach to my
foot and take a step with it but I was
thinking maybe I could miniaturize this
concept into something much lighter that
barely works but doing the math I don't
see any way to make this where it
doesn't just bend and break but then I
just happen to find the answer at the
hardware store this is a collapsible
ladder it goes from a really small size
to a really long ladder and it's strong
enough to hold a person but it's also
really light and portable this is
exactly what we're looking for if we
just remove this middle part we'll have
two telescoping poles that we can build
our stilts
around then if we connect them to our
feet and make them expand we have go- go
gadget legs although at the moment this
is just kind of a dead fish and we need
to find a way to make these expand
automatically I want the legs to extend
by themselves to pull themselves up by
their bootstraps and my best idea which
I kind of hate Kind of Love is
this Air This is called an air cylinder
and it's kind of a mini version of what
I'm thinking about so this is a sealed
tube and inside there's a rod and if I
put air behind the rod it's going to
shoot out like
this and if you think about it the
segments of this ladder look a lot like
an air cylinder that's inside of an air
cylinder inside of an air cylinder
inside an air
cylinder inside of an air
cylinder air cylinders all the way down
if I could just make this air tight
putting air into one end should make the
whole thing expand lift me way up into
the air to do an epic dunk although
saying just make it airtight is an
extremely loaded statement which
Engineers love to do just make it
lighter faster and cheaper just compute
the optimal path that visits each City
once just split the atom it's so tiny
how hard could it be we just need to
make it airtight except for its full of
holes there's going to be a million
seals in this and a bunch of them are
going to move every single one of these
tubes has to be able to slide while
staying airtight and I think doing that
reliably is going to be the hardest part
my general strategy is going to be to
put a rubber ring around each of these
tubes and squeeze it tight against the
tube so that it's sealed airtight but
the tube can still slide underneath this
ring and this is called an O-ring
although the way I've drawn this air can
still go up and out up here so we'll
need another o-ring to seal the top
let's get it
made almost all the metal Parts can be
made on my water jet if you haven't seen
this machine before it cuts metal using
water if you want to see how it works
check out my pencil
sharpeners man these would have taken so
long to
machine Machining metal Parts is the
most work so I try to avoid
it
but there still were a number of parts I
had to
machine that's all the metal parts now
we just have to make all of those seals
every joint requires a custom piece so
it would be way too much work to machine
all these so I'm just 3D printing
them these are the pieces that'll hold
the O-rings they hold the O-rings inside
these
grooves then they slide onto the ladder
and they're held in place with a very
special screw everything has to be
airtight so even the screw has a little
o-ring on it to seal it all right now we
just have to do this for 12 more joints
putting this all together is really
tricky because it's very easy to damage
the O-rings that's all the seals for the
joints and they feel pretty good feels
like this would be airtight although we
also have to seal the ends the little
tube touches the ground and so there's
kind of a foot that goes on the end of
it to seal it and then the big hole on
the top is sealed by this big
complicated cap which has a lot going on
but the only thing that matters right
now is that there a spot where we can
put air in to make this thing expand but
there is a very important question here
which is what makes it stop expanding
because when we put air into this hole
it's going to generate an insane amount
of force trying to make it extend and at
some point it has to stop or it's going
to blow itself apart right so these legs
have a range of Pistons from a very big
one up here to a very small one down
here and this little one is going to
need a lot more pressure to lift me than
the big one it's about 10 times the
pressure which means that when I'm
giving it the pressure to make this one
expand this one's going to be seeing
about 1,000 lbs of force trying to pull
it apart and so the leg has to withstand
that otherwise this is just going to pop
apart there's a plastic cap on the top
of each of the segments which wedges
itself in this sort of circumferential
Ridge on the inside of the tube my
instincts are telling me there's no way
this piece of plastic will be able to
take the forces so we're going to test
it just to see we're going to give it
all the pressure and see if the tube
pops apart I also calculated that the
tubes can take this pressure without
[Music]
rupturing wa well that answers that
question we need something that's going
to keep these from going Beyond a
certain point this is hard because
there's just no room we can't even start
putting holes and stuff because we have
to keep it airtight the initial design
that I came up with was to use steel
cables that would connect each segment
to the next one and they would bend out
of the way when it was collapsed and
then stretch tight when they reach their
limit but the more I thought about it
the more I hated this design so we're
not going to do this I have cable for a
future project what I'm going to do is
really similar but a lot better instead
of a cable we're going to make a sort of
chain out of two pieces of metal
connecting the segments together with
this we'll hold them together and it'll
fold down really nicely all right let's
make it
I have over a 100 Custom Metal parts now
thank goodness I have the water jet
because Machining these would be a
nightmare all of these little rings are
how I'm going to mount the chains to the
tubes without putting holes in them
rebuilding the legs is not fast though
and hopefully I don't blow seals much
because you have to take the entire leg
apart to get to a
seal the question now is if this thing
can lift me and I add a little foot rest
to stand on and I only have one because
these are very timec consuming to make
ultimately I'll have two of them one for
each leg but not until we work out the
Kinks with this one so if I'm successful
I'm going to go way up and then fall
down and I'd rather not land on my head
so I'm going to have an auto ble
attached to the ceiling and attached to
me I'll be wearing a harness and what
this does is it's basically a rope
that's automatically pulled up as I go
up and if I fall it will catch me and
lower me down safely the same way that a
rock climbing bler would work another
danger when this thing is fully extended
it's going to be way up there it's
really topheavy if it falls over it
could punch a hole in the wall which is
why I added this tarp to try to protect
the wall could also land on my head so I
have this rope with a pulley that can
move up but not down the leg will be
attached to this and then if I fall off
it'll just hang by the pulley rather
than falling on me my last fear here is
that this thing is going to punch me in
the face when I pressurize it it's going
to be trying to expand but my body
weight is going to be pushing it down
and if my foot pops off it will shoot up
with potentially a lot of force and it
could hit me in the face I'm not sure
how bad this effect will be so I'm going
to do is pressurize it up carefully and
jump off to see where it
goes
W yeah we should probably do something
about that so here here's what we're
going to do we're going to run a cable
down the inside of the leg anchored to
the foot and it's going to go up and
attached to a winch and it can expand it
in a controlled Way by unspooling it
here's the winch and the very smooth
cable which seals against the cap where
it goes into the leg this lets it slide
through the cap without air coming out
it attaches very securely to a new metal
foot and it winds onto the winch on the
side and wraps over this pulley so that
it goes straight into the leg I think
it's safe to say that standing on the
leg and just letting it rip is not a
good way to test it everything happens
very fast I can't tell what's going on
so I made this roller coaster track that
will guide the leg up and down in a
straight line this will let me be much
more systematic and take things slow it
also should be a lot safer since it's
moving in a controlled way rather than
shooting off in random directions
especially not into my face this air gun
is what lets air into the legs to make
the testing easier I'm running the winch
with a drill yes it works
[Music]

you know what never mind this winch
design is just terrible every time the
leg retracts it goes slack and gets
tangled up and it's really easy to
damage the line and it gets kinked
really the only thing I'm trying to
solve is this thing shooting up
uncontrollably and if that's the main
problem to solve there's other ways to
solve it let's be real this is why they
make helmets
all right let's see if this thing can
lift

[Music]
me so I didn't design the seal fittings
right they're the wrong
shape so I printed a new set which we're
going to install and hopefully that'll
do it rebuilding these legs takes so
long this is the most painful part of
this project for sure all right let's
try it again
[Music]

unfortunately I designed the seal
fittings wrong they just leak still so I
designed and printed another set and
hopefully these ones will work did I
mention how painful this process is but
I think the seals are good now and look
how tall these things things
are
wow I think we're ready to make the
second leg so allow me to present 20
hours of my life in 10 seconds or
less we're still going to use the guide
rail so I'm modifying it to hold two
legs all right here we
[Music]
go so good it
works
I still think this ladder is shooting up
too fast so we're going to connect it to
an auto ble in Reverse this should keep
it from shooting up too
fast let's see how it
[Music]
works that is way better now that it's
not going to kill me let's try dunking
some
[Music]
balls see if we can
[Music]

dunk
[Applause]
easy okay so now there's two questions
how high can we go and can I do it
without the rail let's start by going
high before I get injured we're going
for 16
ft all right so
wow all right on
ballet you can do it
man so this is about the limit of the
legs it's really slow
[Music]
come
on come
on one
more one more oh
yeah

boom I can't believe I just inflated a
ladder to lift me up 16 ft to perform a

completely um uh fraudulent
dunk what a time to be

alive I was doing a bit more testing
when the rail got jammed the force of
the legs completely obliterated the
mount which is really
strong this is a great example of why
I'm so afraid of these things let's make
sure that doesn't happen
again I'm making a new rail guide That's
All Steel
super strong and it should be
unjam basically the same thing as the
wooden guide It's just made of steel and
seeing how strong this is makes me more
confident so I want to see how fast we
can go I upgraded the air delivery
system so that we can get more air into
these things faster all right we are on
blet I'm a little bit afraid to give it
full Chooch here we go whoa oh my
goodness that
is that was faster than I was expecting
that that was freaky all right on ble
ble is on dunking dunk on Full

Speed so

good
[Music]
on
oh that's crazy this is incredibly fun
and it's really cool but I'm not totally
satisfied I really want to see dunking
with a self-balancing set of legs so I'm
going to work my way up to full
balancing starting with this I'm
attaching the stilts to the cart with a
pivot that lets them move side to side
so I'll have to balance in that
direction but they won't let me go
forward and back so it's sort of half
balancing let's see if we can do
it this ended up being a lot harder than
I was expecting I ended up spending
multiple days practicing and then
sleeping on it to try to make it muscle
memory ow what the and after a lot of
practice I can do this there we

go
D that was pretty smooth Maybe I am
learning to balance on these things we
are now disconnected from the rail let's
see if we can balance in all
directions I can't even balance on the
ground I don't know if that's going to
happen man well that was
prophetic I spent hours trying to
balance on this I slept on it to see if
I could get better and I
didn't
oh there is no way I'm balancing front
to back but that's okay cuz I just
realized I'm a
why am I trying to walk around on
peg legs I don't walk around on my heels
I walk on feet I made some size 11 ft
for it which just like my size 11 ft
should help it balance front to back we
are no longer attached to the rail I've
got a climbing rope with a one-way
pulley which should keep it from tipping
over and slamming into my head or the
floor but it's not actually strong so
it's not helping me balance
[Music]

I didn't
fall this still isn't really fair the
stilts are connected together by this
beefy frame and it makes it easier and
they're not stilts I can't walk in them
so we have to do it without
this I could totally walk in these if
they were connected to my feet I
designed these to do that but it's way
too d dangerous so I'm not doing it all
right here we
go no
[Music]

no tell you what you really wouldn't
want to get in front of these
things man that's so scary every
time we're getting there I mean we're
getting there sort of this is really
hard hard and really sketchy we're going
to keep trying but before we do that if
you're wondering how I'm able to make
something like this and have it mostly
work and not punch me in the face it's
really because I've taken the time to
develop a theoretical understanding of
how things work so I can predict what
pressure do I need is this thing going
to explode what are the forces going to
be before I've built anything and then I
can design it so it'll probably work
usually and it's not magic it's takes a
bit of time and effort to learn it which
is why I'm a huge fan of this video
sponsor brilliant brilliant is a tool
that makes it really easy to learn
technical stuff it'll take a subject
like mechanics and break it down into a
series of lessons that teach you the
theory but then have you work examples
so you're learning by doing which is
just the best way to make the stuff
stick the other really important thing
is schedule you can't just read a
textbook for 8 hours once a month you
need to be learning consistently and
sleeping on it which is something that
brilliant is designed for the lessons
are broken down into these bite-sized
chunks which makes it really easy to do
a little bit every day you're going to
be amazed if you do this consistently
how much you learn and they have so many
topics all the math computer science
data science physics mechanics there's
probably something here that you want to
learn so it is a tool that's designed to
make it as easy as possible to pipe
technical knowledge into your brain and
it works really well so if you're
interested in building up your technical
abilities you need to check out
brilliant it's free to try for 30 days
so you can see if it works for you just
go to brilliant.org stuff made here you
can also click the link in the
description and the first 200 people to
do this will get 20% off their annual
premium membership I love having
brilliant as a sponsor because learning
is such an important thing for you and
for humankind so thank you brilliant for
sponsoring this video and thank you for
taking the time to check it out all
right it's time we have to do this so
here we go 12T 1 in world record by the
nerd totally legal totally regulation
here we
go all right we are just going for

it
yes
yes it
works oh my that is
[Music]

scary finally full dunk at speed with
stilts with no help we did it it's the
only time I'm doing it cuz that's way
too sketchy I need to go sit down thanks
for

[Music]

watching"""
    return process_transcript(text)


def process_transcript(text):
    text = text.replace("[Music]", " ")
    text_lower = text.lower()

    text_punct_removed = remove_punctuation(text_lower)

    text_single_block = text_punct_removed.replace("\n", " ")

    text_without_stopwords = remove_stopwords(
        text_single_block
    )  # Comment this if you do not want to remove the stopwords and return text_single_block

    return text_without_stopwords
