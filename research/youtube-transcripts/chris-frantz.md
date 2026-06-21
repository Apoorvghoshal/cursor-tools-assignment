# YouTube Transcript: Chris Frantz

Source: https://www.youtube.com/watch?v=w27JDOb5dDQ

## Transcript

We don't think email belongs in the

codebase. What we have found is that if

you send it all through one place and

you only have one place where the

problems can exist and that helps a lot

with debugging. It helps a lot with

getting things out in into production

and it helps a lot with having a unified

brand. If everything goes out through

one pipe and you feel confident that

it's well managed and well built, then

life gets a lot easier.

>> Welcome to the peel. I'm your host

Turner Novak, founder of Banana Capital.

Today's guest is Chris France,

co-founder and CEO of Loops.

>> Loops is the email sending platform for

software companies.

>> Our conversation gets into why email is

still such a big problem for software

companies.

>> I think people undervalue the value of

email and the amount of pain that it can

cause if it doesn't work. If for some

reason your transactional provider goes

down and you primarily have users log in

through email off, like congratulations,

your application no longer works.

>> Chris spent many years in marketing and

growth. We spent a good portion of this

conversation digging through things like

when to lean into product like growth

versus height.

>> If you want to build something very

good, very defensible, and something

that has the foundations to be a decade,

multi-deade long business, it's unlikely

that you're going to get to that

defensible state in 3 months.

>> Some of the early stunts they did to get

their first users and why they keep it

simple today.

>> We have almost zero analytics. We run no

marketing, no sales. the importance of

good product.

>> The best way to actually improve your

CAC is not to have better ads, it's to

have a better product.

>> His hilariously simple framework for

building products.

>> Talk to users build the product and then

share any updates to the product and

repeat

forever.

>> Building one of the first GPT rappers in

2020 and lessons from selling his first

company.

>> Never let anybody take your own

compensation out of your control if you

can avoid it. breaking all the rules

with Loop's YC application.

>> And he was like, I don't think anyone

said that this year

>> and why Loop's customer support team is

all engineers.

>> You have fewer bugs because if there's

anything that an engineer hates, it's

being told by 10 different people that

this one thing doesn't work.

>> Before we jump in, a reminder, I publish

new episodes of The Peel every week

exploring the world's greatest startup

stories just like this one. Check out

the back catalog of over 100 episodes

like conversations with the founders of

Robin Hood, Product Hunt, and

Browserbase. Now, a quick word from Ramp

and Handover Park before we talk to

Chris. If you're running a finance team,

you know how much time gets wasted on

expense management, chasing receipts,

categorizing transactions, waiting for

expense reports. It adds up quickly.

Ramp handles all this automatically.

RAMP is a corporate card and expense

management platform that over 40,000

companies like Shopify, CBRE, and Stripe

are using to streamline their financial

operations. But here's what makes their

corporate card different. Every

transaction gets automatically

categorized and matched your receipts.

No more wondering what that $47 charge

was 3 weeks later. You can set spending

controls, get real-time alerts, and even

block certain merchant categories. That

sounds pretty cool. It's like having a

finance team member embedded in every

purchase. The platform integrates with

your accounting system in ERP, so

everything flows through without manual

data entry. Whether you're issuing cards

to a few employees or managing spend

across departments, RAMP gives you

visibility and control without the

paperwork. Stop chasing receipts. Check

out ramp.com/theel.

Get $250 and see what a corporate card

can actually do for you. Time is money.

Save both with RAMP. This episode is

also brought to you by Handover Park.

Hannover Park vertically integrates fund

admin, portfolio management, and the LP

experience for finance and investment

teams. Most of you have probably

interfaced with a fund admin provider in

some way. They're a necessary evil for

every type of asset manager across not

just venture, but also private equity

and private credit. They provide

bookkeeping and accounting so investment

firms can report to their investors on a

quarterly basis. What's crazy is they

charge hundreds of thousands or millions

of dollars per year to basically not

screw up your accounting. They sit

together thirdparty software like

QuickBooks, Bill.com, Salesforce, and

Excel and then throw a bunch of bodies

at you. And that's where Handover Park

comes in. They built their own

accounting system from scratch, which

ingests all your firm's data and

documents. And their AI native solution

automates all the manual work that

drives private market investors crazy.

Head to handover.com/turner

and try the AI native ERP for private

market funds. That's h an ov

pk.com/turner

and 10x your fund admin. Chris, welcome

to the show.

>> Thanks for having me.

>> Yeah, excited. Excited to do this. Can

you real quick tell me what Loops is

just for people who who aren't familiar?

>> Sure. Loops is the email sending

platform for software companies. We make

it easy to send email for your software

company. Maybe this is like a rhetorical

question or maybe this is actually a

very important question, but why is that

such a big deal?

>> We think email is still important. Uh I

for one probably get more email than

almost anybody as the

>> the email SAS guy. Yeah,

>> it's unbelievable actually. But we think

email is still important. It's the

primary way the businesses communicate.

And we didn't think that there was a uh

a single company out there whose entire

focus it was to improve the experience

of email sending for software companies.

Um for e-commerce, Claio did a really

nice job. We didn't see anything out

there for software companies and it's

something that we needed at every

company we started prior. Yeah, I think

I've heard you mention before that

there's like seven or eight publicly

traded companies that are just email

sending businesses. That's I mean that's

I I guess it makes sense, but also kind

of blows my mind. It's like just that

big of a of a concept.

>> Yeah, definitely. Um they're not once

you grow to that level, it typically

grows beyond just email as a single

channel and expands to text, inapp, and

push. but attentive, braise, a number of

others. And then of course larger

companies like in it, which now owns

Mailchimp, sold for 12 billion I

believe. So there's there's quite a few

companies out there where significant

portion of their revenue uh is driven

through email.

>> It's sort of if you want to expand a

little bit more, it's almost like a

customer relationship channel. Like it

sounds like a lot of these will expand

into like texting, push notifications,

just other ways you talk to your

customers. So it sounds like if you

really just think about what it is at

the end of the day, it's just like a way

to have a relationship with the

customer.

>> Yeah, it's it's a way to communicate in

a in a medium that isn't controlled by

anyone entity and everyone is pretty

comfortable with. Email is one of the

few good things on the internet at its

core. Maybe not maybe not so much in the

spam inbox and promotionals, but open

source protocol, anybody can use it.

It's getting harder to do it entirely

yourself now, but it's it's a good thing

that exists. And in order to treat the

channel well with the respect it

deserves and your customers as well, we

do our best to install a bunch of

safeguards to prevent any issues with

you hitting spam or you sending spammy

message to your customers. Uh, for

example, our most recent change, we

actually made it easier for your

customers to unsubscribe from your email

list.

>> That sounds like a bad bad thing. Yeah,

it sounds like a bad thing, right? But

our goal is just to make sure that we

respect the protocol both ways. The

result of that also is that your

customers tend to be happier with you.

And if you have an overzealous marketing

person or an engineer who doesn't

understand the current specs around that

stuff, we handle that for you so you

really don't have to think about it. Our

goal is to kind of build the closed loop

for email.

>> Interesting. Is that the significance of

the name then? Because when I when I

first kind of read loops, I thought like

growth loops maybe like you send a email

loops in another customer. You you know

>> that was somewhat the original

intention. Reforge has a really good

program um and or they did a decade ago

and it was um one of their primary

things was growth loops and uh I I

realized at that time that loops.so So

was available. So I purchased it. And

then when we applied to YC, we had three

or four different ideas ranging from

email to privacy to a climate thing.

We chose loops. We picked a domain that

we had already owned and

that's pretty much the story there.

>> Nice. So maybe a little bit just kind of

going a little bit deeper on what you

talked about before, but the way that

someone might lose use loops or the way

that software companies use email. Like

if I'm just hearing this for the first

time and I'm like it's whatever it

doesn't seem like a big deal. Like why

is it such a big deal?

>> What we found is that preeries D

companies, that's our target market

right now, pre- series D software

companies, they tend to use anywhere

between two to five different tools to

email their users, which seems like a

lot, but it does make sense if you start

to think out what those different tools

do and their unique use cases. It's

everything from notifications to product

updates to a newsletter to investor

updates to onboarding and then the whole

world of transactional email that can

easily be represented in a number of

different tools. Our goal is that you

can do that all in set of loops with a

single tool at a single price point. Uh

we don't charge you based on sending. We

don't charge you based on team seats

and we have a single shared set of

editor primitives that you can use

across all those things. So what that

means is your designer can create a

couple shared components inside of one

editor and then your engineers can use

that exact same template. Marketers on

your team, marketers, investors, anybody

who happens to have access to your

workspace and wants to use it can send

with the same exact style stuff that

your designer is happy with.

>> Like traditional email senders like not

work that way? Like do you have is it

because like the marketing team might

use

Clavio, the engineering team might have

like hardcoded some email sending thing

that some guy built because he really

wanted to like because it just lives in

all these different places and you don't

get this like uniform experience.

>> Yeah, it's exactly that. So marketing

might use Mailchimp,

engineering team might use Send Grid.

Somebody else on the engineering team

might use something like Knock for

notifications. your product or community

person might use circle or Substack and

then the founders might use something

well there's a couple dedicated

platforms for fundraising stuff. Uh if

you put that all into one then what you

get is a lot of benefits from the shared

thing. you get like shared access,

shared primitives, shared components,

shared design language.

And it also means if you manage to take

email out of the codebase, then if you

need to update your transactional

emails, it does not mean you need to

loop in the entire engineering team, go

through a PR review cycle and wait until

that process finishes. Let's say if you

wanted to like update, you know, like

the copyright or something in a footer.

Now, a marketer, a designer, or even

somebody on the legal team could quickly

do that and not have to go through the

entire PR review process.

>> Is is that what companies typically do?

Like what percentage is like actually

coding all that stuff into the codebase

versus using a tool?

>> It's pretty high.

It's somewhat of a controversial

statement by us to say that we don't

think email believes belongs in the

codebase.

But what we have found is that if you

send it all through one place, then you

only have one place where the problems

can exist. And that helps a lot with

debugging. It helps a lot with getting

things out in into production. And it

helps a lot with having a unified brand

and understanding of the email

communications that goes out. If

everything goes out through one pipe and

you feel confident that it's well

managed and well built, then life gets a

lot easier.

>> It reminds me of one of those things

that can be email can be tons of upside,

but also tons of downside. Like it can

be a great way to communicate with

people, great way to, you know, sell

something to a customer, recruit

someone, etc. But also like if you send

too many or bad emails, it's a pretty

easy way for people to say, "Ah, this

Loops company, I I hate them." like

block, delete, send to spam, ruin your

authority, never buying your product,

unblocking the founder on on social

media. Like I never want to see this

again because the email was annoying or

bad. So I guess it's like it's uh it's

high stakes.

>> Uh yes, it is somewhat high stakes. I

think people undervalue the value of

email transparently and the amount of

pain that it can cause if it doesn't

work. If for some reason your

transactional provider goes down and you

primarily have users log in through

email O like congratulations your

application no longer works

>> really

>> like that's they can't get into your

platform if they can't log in. Maybe

some of them go through Google off but

if many need two factor off or some type

of secondary confirmation as you see

with like a lot of sock 2 compliant

companies that becomes more of an issue.

So deliverability, uptime, reliability,

all that stuff is key and core to us.

But we think that if you just let us

handle email, we will promise to do our

best to just make sure you're sorted.

You don't need to learn about

deliverability. You don't need to learn

about any standards, dark mode in email,

making sure that uptime is consistent,

that send time is within a certain

period of time, literally none of it.

Just give us the keys, we'll drive, and

at the end of the month, you pay us a

certain amount of money.

It's mostly worked out pretty well. Our

churn above like a certain price point

like when a real company becomes a

company and they have like you know

maybe 5,000 10,000 users is practically

zero. We and we've been around for

around four years now. So we think we're

doing something right.

>> Yeah. Just think speaking about the the

importance of email like I think there's

so many times where I'll buy something

and I'll kind of if I don't get an email

or a text about it, you kind of wonder

did it go through? Like that's kind of

that final confirmation of like you pay

for notion premium and then you get that

email that comes through two seconds

later like all right good I have it the

transaction worked and you're like the

email like gives you like the you know

as a as a customer that it all is

everything's good. So

and it's interesting too when you say

when you talk about like this is a

business. I'm just curious like I'm I'm

sure you probably got this a lot when

you started the company like email like

how can how is that valuable? like how

do you get people to pay for that? Like

what's kind of like the opportunity in

email? Like how much money can you

really make building a company here?

>> Yeah, the our best customers are the

ones that have been doing it for a while

because they have very specific sets of

expectations and then if we meet them

then they're very happy to not have to

think about all the typical things that

come with email.

It's usually the folks that we see that

are most skeptical are the ones that

haven't had their email down for an hour

or two or for days without response from

their provider or have had like DNS

records migration issues and not been

able to un

to fix that. Um

once you've felt the pain, you know you

don't want to deal with it anymore. I'd

say it's pretty much equivalent to like

using a cloud service for your hosting

versus trying to like run the own metal

in your living room. Once you've done

that, you definitely don't want to go

back to how it used to be.

>> What kind of comes after email? Because

like it kind of seems like in my

opinion, maybe other people have kind of

seen the sentiment is like too many

emails out there. We subscribe to so

many newsletters like I don't open

things.

What do you think is kind of like how

what does the future of all this kind of

look like?

>> Yeah, I mean inherently it's it's just

communication protocol for sending text.

So I think it's going to be around in

one way or the other. I'm hopeful and

we've seen it with Gmail since they've

implemented like Gemini Flash and other

models for scanning that the spam and

inbox filtering is just going to get

better and then the stuff that you see

is the stuff that you want to see. Um I

think we're probably going to see a big

shift there. Open rates and click rates

are already garbage. they're offiscated

to the point of not being helpful for an

individual. Uh they're only helpful in

aggregate and I expect even that to

shift in the future as privacy

protections improve which is a good

thing.

>> So how will both of those shift?

>> Privacy protections

such as what Apple is doing with

private email tracking I believe is the

name of it prevents open and click rate

tracking for iCloud users. Um, in the

newest Mac OS Tahoe and the related ones

for iOS and iPad, they actually block

UTM parameters as well in Safari

messages. Most people don't know this.

Uh, it hasn't been something they talked

about, but they do broad sweep blocking.

So, that's everything from like Facebook

click IDs to Google Analytics IDs to to

of course like UTM source, UTM campaign,

which might be used to identify and

attribute an email.

So, I think it's just going to get

closer to sending stuff that people want

to read being the key and then people

will let you know because they will

unsubscribe and that'll be your biggest

indicator.

>> Interesting. It's it's it's getting like

less data driven almost.

>> Yeah. And that's a good thing. I I

mostly I mostly think it's a good thing.

We we have almost zero analytics on our

own site aside from like technical

monitoring. Yeah. I transparently don't

care at all about where people come

from, how they find us,

any of that stuff. We run no marketing,

no sales.

So, how do you know that anything's

working? Because it seems like, you

know, you think of like the typical tech

company, it's like tons of experiments,

all these channels, quantify everything,

analyze everything. You're doing the

opposite. How it seems like maybe maybe

it works, but like how how did you how

did you like come to this conclusion

that this is the way to do it?

>> Well, you need a certain level of

confidence to to realize that most of it

is garbage. So,

prior maybe six years ago, my career up

to that point had been built inside of

like growth and marketing. And I spent

just gobs of money

in in terms of buying. I purchased

everything from like national television

ads to national like metro subway

rollouts to radio to podcast NPR. We

were Linus TechTips biggest sponsor on

YouTube for

>> Oh, nice.

>> six months in a row or something.

>> Which product was this?

>> This was Curiosity.

It's now publicly traded company. It's

Curiosity Stream.

>> I was going to say it's like the

streaming.

>> Yeah. It was one of the first employees

there was a fifth hire, I believe, at

John Hendricks. uh he was the founder of

Discovery Channel and they let the

marketing person go. I stepped into the

role and then just grew with it which

was cool for a long time but I spent a

lot of money and I learned the value of

ad tracking and spending. I mean we

spent millions of dollars a month in

2016 in the heyday of like Facebook ad

tracking and all that stuff and grew a

big distaste for it. And what I realized

is that the best way to actually improve

your CAC, your customer acquisition cost

or your CPA, your cost per acquisition,

is not to have better ads. It's to have

a better product. Everything is built on

the product, right? That's what you're

ultimately selling. If the product

sucks, no amount of advertising is ever

going to save you. It can help get you

in front of people. Like the the Cluey

team is doing a good job of getting

their product out in front of people by

generating hype, but at some point the

product needs to do the work.

So, I think it's important to advertise

a little bit in the very beginning to

build yourself an audience, but at some

point the switch needs to flip to

product. And then if the product can't

grow itself, if if you're in like a B2B

SAS, it obviously varies by industry,

but if the product can't grow itself,

then you probably didn't build a good

product. There's I'm sure there's

exceptions to the rule, but

I think the greatest sign of product

market fit is a company that grows

exponentially month over month with

nothing but word of mouth.

So if I if I'm not growing and my my CAC

is really high, do is it just like you

need a new product like the product

doesn't work?

>> Oh no. I would say if you want to do

like a productled growth B2B SAS that's

bestin-class. Um if you want to build

one of those very specific companies,

this is which we do. That's the path

that you need to take. If you want to

build Docuine, then you need a sales

team.

You need folks in major cities. You need

a bunch of VC capital. you barely need a

product and you need probably a very

rich founder that can bankroll it uh

during downturns.

But that's like a that's like a that's

like a sales go to market. You know, if

you want to do product, it's got it's

got to product first. It's got to be led

with product. Otherwise, you're not

building a product first company.

>> Yeah, that's true. There's like two

lenses. It's like salesled versus

productled.

>> Well, there's also like hypeled,

which we'll see how long it can go.

>> Is that is that real? Like is that even

a is can you make a company with

hypeled?

>> Uh I think mischief did that for a

little bit. I don't know if it's

sustainable long term is is what I would

say. Maybe like Red Bull is potentially

the closest. Like right now there's like

the world's like largest skateboard drop

in happening right now. It's like up on

a skyscraper. It's currently being live

streamed. Millions of viewers. And like

they've just been doing this for like a

decade, maybe longer.

>> Yeah. I mean like 20, 30, 40 years

almost.

>> Yeah. It's been a long time, right? So

maybe hypeled is possible, but it's it's

hard.

>> Yeah. I mean, if you even think about

it, like

a lot of things kind of are hypeled.

Like when I even think about sports

leagues, like the NFL, right? each week

it's like oh this big matchup between

you know the Chiefs and the Bills like

you know it's like a it's the the first

opening game of the season is like a

Super Bowl rematch or like you know it's

the two undefeated teams are playing

this week or like this guy's trying to

break the record for the new all-time

passing leader in week 15 or 16 or 17

and then you know like in the offseason

it's like a draft and like there there's

like always these like almost like big

hypable moments and if you kind of

relate it back to startups it's like

launching a new feature, new product,

new employee joining, we hit a

milestone. You know, there's always

these new things that are kind of

happening and and that are all kind of

their own hype moments really at the end

of the day.

>> Yeah, there's there's good coralaries

between sports teams and startups,

especially right now when salaries are

very similar for star players, I would

say.

>> Yeah. Fair.

>> Yeah. I mean with with with football or

basketball like the the core product

there has been refined over a long

period of time over a lot of scrutiny

against audiences like literally tested

against audiences.

Teams have been drafted just the best of

the best. So um the hype cycle supports

it but no one's going to watch a

multi-hour game if it's like littered

with commercials if it's actually a

terrible product.

>> That's thing I think is incredible about

the NFL. It's like if you if you think

about it, it's like a threehour TV

segment with like 4 minutes of actual

gameplay with just it's like the perfect

vehicle for delivering ads to the

average American. Like just an

incredible business product in that

sense of just you've been able to shove

so much so many sponsorships into it.

>> Yeah. Chat GPT2 will be a better ad

model.

>> Oh yeah, fair. In the sense of you can

weave monetization into that a lot

better than like traditional Google

search. Absolutely. Yeah. All they need

is a disclaimer here at the bottom and

where it says information may be

inaccurate, information may be

inaccurate and contain promotional

material and boom, that's it. And you

can put ads in. You don't even need to

disclose them past that point,

especially with our currently like

defanged FTC.

>> Interesting.

So, what do you what's your opinion then

on how valuable chat GPT could be? Like

how much how much revenue could that

product do at scale? Like more than

Google? I I don't know that I have the

answer for you there.

>> I mean, it probably could.

>> Yeah, potentially. Potentially. I mean,

the outside bet though, right, is like

AGI swoops in and then and then why do

we have chatgbt?

>> True. Just all pipe into our brains. We

don't even need an interface.

>> Then the rate of progress happens

exponentially at that point. So,

you know, brain inference becomes

something that is no longer sci-fi and

very fast, right? So like in a very real

way like why does chat GBT exist if

knowledge multiplies every second?

>> Yeah, that's true. We're going to hit

we're going to hit postn knowledge post

AGI postn knowledge economy.

>> Yes, but there will be email.

>> That's true. A good way to tie it back.

So how did you initially kind of like

come up with the idea for loops? I'm

assuming

you came across this problem over years,

but like how did it kind of all evolve?

A couple companies ago, we were paying

one of the aforementioned publicly

traded companies

a couple hundred,000 a year and it was

part of like a three-year annual

contract, right? It was no longer just

like annual was like three years. It's

very common in these publicly traded,

previously listed companies.

>> Is that a pay upfront model? Like you

pay upfront for the three years too?

>> Uh it depends. It can be structured in

lots of different ways. Yeah. Yeah. they

they they have legal teams that are the

size that there's sales teams and the

engineering teams are a fraction of

both.

So I I wasn't happy with that model at

all. And then

at our previous company that we sold, we

were using Mailchimp and Send Grid. Uh

we were paying Sen Grid like $100 a

month and we were paying Mailchimp

$1,500 a month. So $1,600 a month total.

And

and the services didn't speak to each

other at all. So we had no idea if

somebody got an email in one place, not

the other, if if the customer synced in

one place, not the other, what the

design looked like in one versus the

other, if that design rendered the same

everywhere, and it was just it was

Mailchimp, right? So I remember when we

went to cancel the account after selling

the company, the pop-up ad that I got

and stuck in my head was like, try our

new postcard delivery and I was like,

what is this is not where I should be

spending my money. This is clearly not

being built for me. Like this might be

great if I was traveling. I didn't I did

not understand who this this ad was for

at the time. So, anyways, that was that

was annoying to me. And then I kind of

banked on. I was like, "This doesn't

integrate with any of the tools that I

need. It doesn't fit into any of the

flows. The templates are all about like

like creating matcha lattes or something

and sending out to your coffee store

customers. Like, it's not built for

software companies." And at the time,

nothing was. So, that's kind of how it

happened.

>> Yeah. I think you and it's sad when I

look back at my email or my DMs. like

you had DM'd me at some point when you

were around when you started the company

being like, "Hey, we're raising a little

bit of money if you want to chat." I

think I saw like a year or two later, I

remember responding. It's in there in

our DMs. I'm like, "Ah, I think I'm

going to regret missing this, but I hope

it went well."

>> Hopefully not. Hopefully that guy fails.

Then I'll be right.

>> Yeah. Yeah. That's always my mindset as

a VC. Like, I hope these guys [ __ ]

lose. I I hope they fail. Yeah.

>> You need the heristic, right? Like you

need some you need some reinforcement of

the negative belief. Otherwise, you're

just giving money to any schmuck that

walks through the door.

>> My anti- portfolio on email news or

email providers in general apparently. I

just need when I meet them, I just need

to invest obviously

>> potentially. Yeah. Yeah. The the

heristics are hard there for sure. I've

invested in six companies and three of

them have actually had series A's. So

>> that means successful. Yeah. That's

that's all that matters, right?

>> Right. Yeah. It's hard to know.

>> Of course not. But yeah,

>> wildly different degrees of valuations

too.

>> Fair. Yeah. Which which can and can't,

you know, doesn't and doesn't mean

things like sometimes that's a good

thing, sometimes that's a bad thing. The

best companies are sometimes always

overvalued,

but that's also something you'd say in

2021 or 2025.

>> It's it's it's very hard to know. The

only thing I would I'm happy about being

very right on is NFTTS were garbage.

>> Yeah.

I feel like I got a lot of

internet views and followers from

commentating on the NFT mania which was

a interesting time in the world.

>> Yeah, I have a mental log of everyone

that took a bite with Crazy Bill and and

and lost their minds and uh I I remember

we all remember we know what you did. We

know what your avatar looked like. I

think my my favorite thing though is I'm

probably one of the only people on

Twitter that still has an NFT as their

profile picture because someone made

this fake NFT generator where you could

have a normal profile picture that

wasn't actually an NFT but it had that

like I don't know he hexagon octagon I

don't even remember I think it was six

sides that you and it would make you

like a six-sided NFT profile picture

without actually being an NFT and I did

this like four years ago and I've never

switched it and they made it so that you

can't do that anymore.

So you like the only people that still

have these NFT profile pictures are

people that have had them for the last

four years and they I mean I haven't

seen one in I don't know a year. So I

might be one of the only people

remaining on Twitter with an NFT picture

and it's it's fake. So

>> Oh there you go.

>> One of the things I'm proud of.

>> Well I think Stripe's doing some like

pivot back to blockchain or something. I

don't know. So maybe it's maybe it's

coming in vogue I guess is what I'm

saying. Yeah. Can you Can you make an

email an NFT? Was that ever a thing?

>> Ah, man. I bet you could. Anything can

be an NFT. You might be an NFT.

>> That's true. This whole this whole

podcast might be listening to an NFT.

>> Yeah.

>> Yeah. Don't hit me, bro.

>> So, well, so getting back on kind of

when you were starting Loops, I think

you had just come off selling snazzy AI

was the other company. And then, so

yeah, what's kind of the story there?

>> We got really lucky in that

Nobody really seemed to care about chat

GPT uh or sorry it wasn't chat GPT at

the time it was open AI. It was GPT3 and

a half at the time. We had played with

GBT2 but GPT3 and a half hadn't quite

come out yet but there was like whispers

of it and I had seen like a couple demos

and then I shot Gregory Brockman an

email just randomly never spoken to him

before. I was like, "Hey, could I get

access to this?" Um, and he was like,

"Yeah, sure. We're doing a batch of like

10 companies to get first access to it.

What are you working on?" I told him and

he was like, "All right, yeah, we'll

give it a try."

>> What was it for people who don't know

>> that you were making?

>> Oh, yeah. Oh, sorry. Yeah. So, we were

making Snazzy. It was snazzy. And it's

currently owned by Unbounce. I actually

haven't visited the site. maybe

redirects them, but it was

AI marketing copy. Well, whatever I

never felt very strongly about it was a

problem that we were really solving. It

was more of like cool technology. Let's

come up with a way to position it. So,

we were one of the first GBT rappers,

which is cool. It was in the same batch

with us was Copy AI,

Jasper,

and

There was a couple others. Several

others fizzled out. I think Jasper is

maybe still going. They've pivoted like

three or four times since then.

>> Yeah, I think I actually remembered I

think someone said some really kind of

mean things about them on the internet.

I saw the founder. I forget his name,

but I think he actually replied and he

like shared some of their metrics and it

seemed like they had I don't know they

were doing relatively well all things

considered. It's like a really long

reply too on Twitter. So I was like,

"Huh, it's kind of cool. They've like

they've n they've navigated it to the

best as they could. Yeah.

>> Yeah. Yeah. I we didn't have any real

desire to continue in the market, but

the business was growing like gang

busters. We were one of the first B2B

companies to spend money on TikTok.

What I noticed is at the time, right, I

was like, "Okay, so we plugged this

model in and there was no guard rails,

right? It was it was awful.

None of the tooling built that we have

today. that makes it so easy. But like

once you like one in 10 responses we got

back was usable.

And so but but once you plug that in and

once you get it in then the core product

itself is just maturing on the model

side. Um all you're doing is you're just

rebuilding the tooling around it and

making things nicer. And once we

realized that the dev stuff was mostly

done aside from like the normal asks

people want like reset password and

invite your team members and all the the

normal SAS strappings. So then we had a

ton of revenue coming in very rapidly

literally within a couple days and then

I just started piping it all directly

into Tik Tok creators and this is pretty

early. So this is like 2020 or something

2021 maybe. Was this in like kind of

like influencer marketing or was it Tik

Tok's programmatic?

>> No, it was all in this was before that

existed.

>> Yeah, there was no ads on Tik Tok and

there was no programmatic I buying

platform or any of that stuff.

>> She was just like DMing or like emailing

creators. Well, I found one person to

run the account and I paid her $1,500 a

month and she ran our account and we got

tens of millions of views very rapidly

in like a couple weeks and then she

started finding other creators and then

she would find them and then we would

pay them and that was it. And I would

just pay her $1,500 a month and I would

pay these various creators directly

however much per video and it did gang

busters. Literally, there was nobody

else out there that was doing anything

like this. We could have scaled it and I

should probably be on a yacht right now,

but

it wasn't a good product per se. Like

we're trying to build a very good

product right now with what we're

currently doing. It was a good way to

make money to make some person happy, I

think, on the user side and to rapidly

scale, but it was never anything else we

were proud about. Uh, we sold it in

under a year for a seven figure sum to

Unbounce who like glued it into the core

of their platform. and

now they're very AI forward and all of

that good stuff. I hope it's going well.

>> I meant to look Unbounce up because I

before this, but for for me and also

people who don't know, it looks like

kind of like a marketing landing page

builder and looks like they've probably

kind of evolved from there over time.

>> Yeah, Unbounce uh back in the day was

the premier landing page builder on the

internet actually. Um, so if you were a

marketing team, you were building them

with Unbounce.

>> And there's supposedly kind of a big

post out there. I've heard you mention

in another podcast, but I couldn't find

the post. But I think you kind of you

kind of talked about just the process of

of selling it. Was there anything big

that you kind of learned through the

process or

>> uh it came inbounds and it closed very

rapidly.

If I was to do it again, and I don't

know that I ever will with our current

company, but if I was to do it again, I

don't think I would have tanches of any

kind.

>> Tanches in the sale process like in the

way proceeds are received.

>> Yeah. So, we got the proceeds up front,

but then we had like tanches based on

like revenue goals internally for also

running the company aside, the main one.

And I don't think I would ever agree to

something that impacted my compensation

in any way in a way that I wouldn't have

100% control over.

So I I mean that very high level, but

yeah.

>> Yeah. I' I've run into that before with

acquisitions where company's acquired,

it becomes kind of tucked into a part of

another entity and then that your

acquired the acquired company inside the

other one has like a specific target

that they need to hit. But then let's

say like the founders are not involved

in it. So like you have no control over

actually hitting those targets. And in

all reality, if I'm the acquiring

company, I'm probably going to make sure

you just barely don't hit them enough to

pay you anything. Like the incentives

are not aligned for you to actually get

those targets, especially if people are

not involved who are being compensated

by them. So that's something I ran into

personally with one of those with a

portfolio company that was acquired. I

could I mean I can imagine that that

could go a lot of different ways.

>> Yeah, I I think it depends on the on the

relationship that you have, the company,

the goals that are created and all of

that stuff, but high level never really

let anybody take your own compensation

out of your control if you can avoid it.

>> Yeah, that's fair. And you're and you

completely kind of bootstrapped that,

right? Like you didn't raise any outside

capital for it?

>> That was bootstrapped. We had investors

but there was no real or we had investor

interest but there was no real reason to

take that and then after selling

we didn't know what to do after we left

Unbounce and I stayed with the same

co-founder we applied to YC we had

applied once prior the two of us four

years prior and we didn't get in so this

was the second application and like I

said we had a number of different ideas

from privacy to climate to loops for

email and we got in they were mainly

interested in loops I was our biggest

pain point and where we had the most

experience as well. We built something

rapidly and saw some early adoption and

decided that was the way to head.

>> Nice. And what was your application

like? I know there's kind of a you put a

ton of work and tons of research into

it, right? And spent tons of time.

>> I spent No, we spent very little time.

Yeah, I recommend I didn't even know you

could ask for referrals or

recommendations or that people prepped

really hard for this. I guess I was

maybe a little naive.

The first time we applied like I guess

now like 12 years ago or something,

we like drove to like a place and we

like found like a sequester quiet room

and blah blah blah. We like tried hard.

We did a couple takes. This time Adam

texted me like 20 minutes before it was

due. Hey, should we try and do like YC

this year? I was like, oh, I don't know.

And then we just like knocked out a very

quick application. We did a quick Zoom

call because it was like 11:00 p.m. or

11:30 or something. And we just like

told jokes at the end of it for like a

couple minutes, way over the amount of

time that it was supposed to run. And

then we uploaded it and that was it. And

then yeah, we got an email shortly

after. We did that and we did the

interview process. It went on for like

40 or 50 minutes. It was Michael Cyel

and Brad Flora and somebody else.

And then

that night we got a phone call and they

said we got in and I said I'll have to

think about it.

Was that like a negotiation tactic

almost or?

>> No, I was like, I got to ask my wife. I

was like, I don't know, guys. Like, this

seems like a big commitment. Let me let

me check with my wife and make sure

she's cool with me having like a

three-month sprint right now. Like, we

have a we have a newborn. Like, there

there's a lot going on.

And he was like, I think Brad who

called, he was like, I don't think

anyone said that this year. We usually

just get a yes. And I was like, okay,

sorry about that. Let me call you back

though. And then yeah, so then I did and

my wife was like, "Yeah, of course

you've wanted to do this for a while.

You should do it." And that was it.

>> So why did you do it? Because you kind

of been historically you've always kind

of bootstrapped.

We, you know, YC is a pretty big

commitment. Sounds like it would be

almost like inconvenient to go out

there. Like why do it?

>> Uh well, we didn't go out there. It was

COVID. So it was a co batch and I did

it. That was one of the reasons that we

decided to apply as well is because my

co-founder Adam is in upstate New York

with his family and I am in a small town

in Maryland outside of DC with my

family. Um, we both have very nice lives

that we've built and they are not inside

of San Francisco.

So, we saw an opportunity there for

maybe attending remotely and uh decided

to take that.

>> Yeah. I've heard you describe it as kind

of it's like a no-brainer if you want to

build a big company. Like why why is

that? Oh, because

honestly sometimes I wonder if like if

it's an IQ thing or if I just see things

very simply or you know like I wonder

which side of the bell curve I'm on, you

know, but

>> because there's like arguments you you

see people arguing extreme on both ends

of the spectrum of why you should or

shouldn't do YC or the value of it.

>> Yeah. I think I think you can just look

like statistically YC tends to make good

bets.

So, if you want to be considered a good

bet and and statistically have a good

chance of succeeding, like maybe then

you should do YC.

It seems pretty clear to me, right? Like

people go to Ivy League schools for like

a chance of success. It's barred for

entry in various ways, but all of these

things are good indicators. If you pile

on more good indicators, does it mean

that you're going to be a success?

Absolutely not. But does do other

successful people have those similar

indicators? Sure. So why not pattern

match yourself?

>> And you I think raised a little bit of

money like around demo day or before

demo day. I think that's probably when

you when you DM'd me.

>> Yeah, we raised we closed around before

demo day like uh I think a week and a

half two weeks before

Yeah. And we raised from a number of

different angels and investors and

generally been very happy. We made it

very clear hopefully to our investors

early on that the best investor for us

was one that just let us build our

business and we didn't have to engage

with too much.

We don't think an investor is going to

save or build or do anything meaningful

to the company. And if they do, then

that's nice, but it's not something that

we should spend any time trying to make

happen because that's not repeatable and

it's not something that like I'm going

to get any real value of at this stage.

Postp product market fit, maybe when

we're like readying for IPO or we're

like collecting funds and doing all that

good stuff and we actually need a

serious bankroll. Sure. But like no

investors like flying to customers

offices all across the country off like

a $500,000 preede or something, you

know, like there's varying amounts of

commitment and stuff and what you should

expect. And I think at the precedency

stage, your investor commitment and

expectations should be very low and it's

up to you to build a good company and

then you know you guys can reconnect and

see what that looks like in the future.

>> So then how did you kind of sus out or

determine who you wanted on board? Like

was there a certain way you thought

about who you should bring on? It sounds

like it wasn't necessarily based on, you

know, like a value ad, per se.

>> No, it was 100% of who I spoke with and

who I enjoyed speaking with. Uh, we

talked to 40 investors.

Around 32 or so were interested in

investing in us. So, we turned on the

majority of them. It was who I enjoyed

getting along with, who who understood

the expectations. We had a couple

investors who thought that they were

doing these really big evaluates. like

we'll be in the office every day. We'll

be the first person you talk to in the

morning. We will text you on the

weekends. I'm like, I like I will

literally pay you to do none of those

things.

>> Please, please, I like I'm not a child.

Like, please no. Um, so it was just

people who like understood what it ended

up being was like a bunch of very

successful founders. That was one of

like the qualifications. It's like you

ideally you founded a company in the

past. And then folks that kind of

understood that it wasn't their job to

make our company. It was our job to make

this company. And as a result of that, I

send an investor update. I get some

emojis and some LFGs and that's about

it.

>> Rocket emojis. Yeah.

>> Yeah. If I need funds or something, um I

I I'm confident I could hit up any of

them and get any amount that I needed to

bridge any period of time. But like

we've been cash flow positive for a

while. We're growing. We don't need any

additional funding. And I think they

would more be confused as to why I was

asking than anything else.

>> Yeah. I think a lot of people don't

realize that the the VC high touch and

like always, you know, being in front of

the portfolio companies, it's really

more for them than it is for you as a

founder because as an investor myself,

like I kind of need things to talk about

to my investors. Like I I mean, you're

so removed from everything that's going

on. Like really what you do is you give

money to some founders and then you just

it's like Jesus take the wheel. Like you

just wait. They either die within like

one or two or three years or it's like

10 years later and it's like hey this

might maybe be worth something but like

you don't actually know. So I mean as an

investor you get data points. It's like

oh these loops guys like oh Chris is

just an animal. like he's always

shipping like you're always in front of

customers and you like need you need

data points to go back to your investor

so that they think you're you're good as

an investor like oh they're spending all

this time with loops they're adding all

this value to Chris and the team and

like you know they they know how

valuable this company is and we know

we're going to get a lot so I mean to

your point it's really annoying so it's

like I think it's as an investor it's

like finding that balance of just like

how can you get that from the portfolio

like oh loops is they're tracking really

well like these guys are on a good

course. They're doing well, but I'm not

being annoying to the founders and

texting them every morning and trying to

go to the office and help them write

code or something or introduce them to

worthless customers or candidates or

>> Yeah. I mean, look, I'm sure that's

helpful for some founders and maybe I

don't speak for the majority of them. I

think if we're gonna like like VC side

talk for a second, I think what standard

Dalton and and co are doing with

Standard Capital is interesting and

that's probably as close to perfect from

a venture fundraising vehicle that I've

seen so far. So Standard Capital is

offering like just a form that you fill

out similar to like a Y Combinator

application and then they grant you some

amount of like series A funding if it is

accepted. That's pretty much it. I think

that's great for series A.

I actually think that you could go even

further with it. If I ever clear loops

or have any amount of free time, I've

always wanted to do a separate fund

where I just do my best to mirror Y

Combinators investments because

historically they have fantastic

returns. So, I think you should probably

just make a form on your page that just

grants safes to any Y Combinator alumni

up to a certain amount of money until

the fund exhausts and that should be the

extent of it.

>> That's a use case for NFTs. You get your

YC safe as an NFT and you you submit the

NFT. It's like, oh, proof of proof of

stake, proof of whatever they call it.

>> Jesus Christ. It's a legal contract is

proof of stake. Yeah,

>> proof of safe is probably what they call

>> proof of safe. Oh, yeah. Sure. Yeah.

Yeah, there's something there. Yeah. If

YC ever launches like an O with YC Oath

function, I'll spin that up. I'll raise

a couple million dollars and then I will

throw up basically like a self-funding

fund that only invests in YC companies.

Everyone gets like a percentage of the

fund and it's done as safes. It's a

single click. You get a docu sign in

your email. Nothing further besides a YC

oath. I don't want to even hear your

company name, what your idea is, any of

that stuff.

>> Yeah. And so, one thing interesting that

you said, maybe you mentioned this to me

earlier, maybe we were recording, but

you you skipped a series A, like you had

an opportunity. I think you maybe you

said you got a term sheet. I can't

remember if this is specifically what

you said, but can you just explain that

to me, that whole process, and why you

chose to do that?

>> Sure. So typically, I say typically as

in like maybe five years ago or so,

folks looked at term sheets for or folks

looked into raising series A when they

hit a million dollars in AR. That was

the that was the usual benchmark. So we

cleared that a while ago and we did look

at fundraising, but I've

I've I've never felt that we had product

market fit. Um I think we're probably I

mean we're obviously the closest we've

ever been, but I still don't think we're

quite there yet.

I on the flip side, I can think of maybe

like maybe five or six companies that do

that I've seen

besides maybe like a local bodega or

something that's probably a pretty good

product market fit. But

we we didn't get there with where I

thought we should be from product market

fit side of it. So, we chose not to

raise funds. Cash flow positive and

we're growing a rate that allows us to

continue to hire and continue to build

product and acquire customers without

having to do any marketing or sales.

When we hit that product market fit

stage, we might look into it or we just

might keep skipping until we end up at

IPO acquisition or I retire.

>> And you mentioned the million-doll

series A benchmark. Is that is that

still true today? What do you think?

What do you think kind of the current

market sort of looks like?

>> Uh, I don't know what the current market

looks like. It seems insane.

I talked to folks and it seems like

borderline NFT crypto levels of insanity

out there right now.

>> Why do you say that?

>> Just because people are raising series

A's in like 90 days, that kind of stuff.

90 days of from like company inception,

that kind of thing. And if you can build

something, even if it's a model, and it

takes you three months to do it, then

other people can build something similar

in three months, and we spent a year and

a half on the product before we launched

it.

Now, that's not to say that we've built

a better business or that that we've

allocated our time well or any of those

things.

But if you want to build something like

very good, very defensible, and

something that has the foundations to be

a decade, multi-deade long business,

it's unlikely that you're going to get

to that defensible state in 3 months.

OpenAI been around for like six, seven

years or something before they launched

at GBT. It takes a while to build a good

thing.

So if you see college freshman

building something in three months and

then knocking down like 40 50 60 $80

million series, hey, you know, maybe the

market's a little little frothy.

>> Yeah. What would you recommend then to

that college freshman? Like should they

not go through that process of, you

know, launch video, some hype, raise a

bunch of money? like what advice would

you give to that person or to yourself

if you're back in that moment?

>> Uh I think it's a great way to

potentially build wealth very early on

in your life. I Yeah, I mean it's not

clear if if the goal is experience, if

the goal is to build a good business, or

if the goal is to make a bunch of money.

And I'm sure if you're 22 years old,

maybe you don't know the answer either.

You're just doing what feels right and

what makes sense in the moment and what

investors are willing to give you money

for. And investors are so scared of

missing out on the next scale or the

next OpenAI.

They're chasing everything that has AI

at the end of the name.

>> And it's interesting because I think you

said you have a lot of customers that

are AI companies. Email is still pretty

important even in this era of you know

post AGI.

>> Absolutely. Yeah. We have lots of uh we

want to build email for modern software

companies. Most modern software

companies today are building with AI at

the core.

So we have companies like Replicate that

build on us and then we have also

companies like that are a little bit

newer like Granola and

just the other day I saw Orchids uh

who's like the top of the web design

benchmarks was it was funny I saw them

because Dylan from Figma tweeted a stat

that they were number two in and Orchids

was number one.

>> I saw Orchids was number one. Yeah, I

saw that.

>> Yeah. And I was like what's this

Orchids? And then I was like wait isn't

that familiar? And then I checked my

inbox and I was like oh yeah look at

that. And they're using loops. So yeah,

so the best modern

companies today are choosing to use us

as well, but we have no AI features.

We're not built especially for AI, but

we have built a very robust, very

stable, very nice to use platform fueled

entirely by a technical team.

>> How did you first get people to start

using it back in 2022?

>> Right. Well, we did spend a year and a

half building this thing. So

>> So was this 23?

>> Yeah. Well, so YC kind of requires you

to get revenue while you're gonna um I I

don't know it's a requirement. It

certainly felt like it. Michael Cyel is

a is a scary dude.

>> If you don't get revenue

Yeah. Well, I don't know. What's the

threat? What What's the threat that they

give you? Do they just like just make

you feel so disappointed that you didn't

get revenue and you just you like feel

pressured into it?

>> There's some level of competition,

right? Like you might be like, "Oh, I'm

better. Take a while to like build blah

blah blah." But like maybe somebody's

next to you and they just hit $10,000,

you know, and a couple days ago they

felt the same as you and now they have

$10,000.

And every week we would meet up and we

would compare revenue like and Michael

Cyborg would oversee it in our small

batch and we would put it on a

spreadsheet and everyone would look at

the spreadsheet and you did not want to

be last on the spreadsheet

and he was he'd be like, "So why why do

you have no revenue this week?" And it

would be like well

reasons. And you'd be like, okay, fine.

And then you go to the next person and

then they wouldn't have those reasons

and they would have revenue. And you

were like, well, why was my reason good

enough? And you start self questioning.

And then eventually we just built

something that users could use. It was

very small. And again, we stayed in like

building, stealth, weight list, whatever

mode for a year and a half. We had users

paying us, but it was a very small

amount. We handpicked them off of the

weight list.

And it was just to make sure that the

numbers continued to go up and that we

had users using our software so we were

not building in silence.

>> Then how do you get people to start

using the weight or get how did you

first get people on the weight list?

>> Yeah. I if you don't have a product you

do need something in order to get people

interested. So we tried a number of

different stunts. So some of that hype

stuff it's it's I think it's a great way

to kickstart an audience if you don't

have one already. So, we purchased a

billboard in Times Square and then we

let Y Combinator startups put their ads

on it throughout the day. Uh, we had a

photographer posted up that we hired off

of some tech who took pictures

throughout the day and posted it through

our company Twitter account and tagged

the companies. That worked really well.

We sent a bunch of swag out. One of the

more fun things that we did was we did a

a serial box called serial called Loops

like in the old Airbnb style. Airbnb

released uh like McCain Obama serial

boxes when they were trying to like

generate some interest and hype. So we

did that for us, but it was just for the

company Loops. And inside of it, we put

a 3D printed decoder ring. So then when

you solve the decoder ring combination,

it takes you to a private URL. And when

you figure out the puzzle in the private

URL, you get air dropped a hoodie.

So that was like really absurd. And it

was like professionally manufactured

boxes. I hired like a great designer.

like we didn't have a product to sell,

right? So, I had to spend my time and

energy on something.

>> It was a box of loop cereal that had a

decoder ring and then you had to decode

the URL. When you went to the URL, you

were sent a hoodie to your house or to

your location.

>> Yeah. It was like way overbuilt. We sent

we did like a couple hundred of these,

right? Like,

and and it worked. Like a bunch of early

customers were like just like this is

like a cool nerdy thing. Like, I get a

box of cereal uh with a decoder ring in

it. I don't know what the decoder ring

is going to do. And a lot of them just

kept it and as like memorabilia. Uh so

and they haven't even opened it. We

actually have like a surprising amount

of hoodies for the amount of boxes that

we sent out. So we still have like a

surplus of hoodies, but I think all the

cereal is gone.

>> Interesting. Well, there's a one the one

strategy. I mean there were some

startups in 2021 that would like they

would sell the hoodies like they'd sell

merch. It was like software companies

that had more merch revenue than product

revenue I think.

>> Yeah.

>> If you remember those days.

>> No. No. Fast. Fast.

>> Oh yeah. Yeah. There's one called Fast.

>> They were doing one color hoodies.

>> I mean, they they did a very good job at

generating hype back in 2021.

>> Yep. And where are they now?

>> Yeah. So, I guess it's like hype can be

good.

>> Hype can be good. You got to have the

product though. Got to back the product.

Yeah. I think I think it's a little

different nowadays because hype

gets you to a place where your product

is in front of users and if those users

haven't used anything like that solution

before and if it's you know essentially

a wrapper of a foundation model then you

can do some like very interesting things

and then I think if you just only focus

on hype and you have a very thin UI and

you let the model providers focus on

improving their model then you act as

this like hypeforward middleman. And

that is maybe an effective go to market.

Like I don't think we've ever been in a

place quite like that before where the

product itself continues to improve and

it's entirely out of your hands because

as it gets better, your product just

gets better and you don't have to do

anything but continue to pay them. I

don't know that there's ever been a

technology equivalent of where we are

now. So you really could, if you were an

AI forward company, devote all of your

time entirely to marketing and hype,

sales, and probably still have a decent

business model until AGI wipes us all

out.

>> Yeah, true. We got about two years. I

feel like we've had about two years for

about two years now, but we probably

have about two years until AGI wipes us

all out. Maybe it's a year and a half.

>> I think the timeline updates depending

on anthropics funding cycles. Yeah.

>> Yeah. I mean that's a another unknown or

sorry another

in my in my and I think it's like an

unspoken secret of like you just look at

the language that comes out from a lot

of these guys of like you know what what

are their what are their incentives

around the claims that they're making.

Um like I think there's the classic

anthropic uh Daario has like some clips

that have gone viral about like you know

six months from now 90% of all coding

will be done by AI and it'll be like

exactly six months later someone will

repost it and it's like you know but

yeah lines up with the funding cycle. So

do you think is it easier to get

attention or build a product then? Yeah,

it's it's much easier to get attention.

You can buy attention. Um, if you have

money, you can just pay somebody with

influence and then you have attention.

It's it's a very simple transaction.

There's a largest companies in the world

are built around that. Facebook ads

which falls into Instagram as well and

then of course Google ads which is

digital oil if you will. So yeah, it's

definitely much harder. It's very

difficult to build a good product for a

specific audience that continues to

improve and satisfy that audience. If

you want to play in hard mode, do it for

a combination of user demographics. So,

we build for designers, for engineers,

for customer success, and for marketers.

And pleasing all four of those types,

it's pretty difficult.

>> So, how do you kind of describe sort of

the cadence of building loops? Like I

think you I think it might be your

pinned tweet on Twitter or maybe you

just tweeted it the other day, but what

how do you just kind of think about just

like the general flow of just what

building the company and building a good

product like that looks like?

>> Yeah. Um so I think it comes from the

organization level. So we have entirely

technical staff. There's nine of us who

were um remote and what that means is

that everyone is familiar in

communicating

in in in like a purely digital way which

means that our

our paper trail for any feature for

support for any of that stuff is

immaculate. It's never like somebody

tapped me on the shoulder and said this.

It's always written down and there's

paper trail on the line. So anytime that

there's something needs resolved, it

resolves very quickly. It also means

that we have 247 global coverage, global

technical coverage,

which is fantastic because it means that

we're able to speak to like corporations

that are in international places that

would otherwise be difficult to support.

And

probably the best part is is if you have

engineers do support, you have fewer

bugs because if there is anything that

an engineer hates, it's being told by 10

different people that this one thing

doesn't work and they are the person

that can fix it. And if they fix it,

then those 10 people will stop talking

to them. And it's been a very effective

way. It does

I'd say it's probably not a fit for all

people on our team, but it is part of

how we run the company and it is

important. So we think all you really

need to do is talk to your users, build

the product, talk to users, build the

product, and then share any updates to

the product and repeat forever

>> until

AGI.

>> Until AGI

>> or heat death of the universe.

>> Yeah. Yeah. Heat death, IPO. Yeah.

>> Yeah. Once you IPO, that's when you stop

stop talking to them and you can

>> Well, yeah. That's when you start

talking to shareholders, not customers,

they're shareholders now.

>> Oh, yeah. True, true. And yeah, I

thought that was kind of interesting

when I heard you say that you have all

the the customer support team is

engineers. You also mentioned you don't

use any AI customer service or customer

support things. Is that still true or

was that true?

>> Yeah, it's well we don't have like an AI

chatbot. What we do use now is a tool

called Zeus by Atlas. It's good. I think

it's pretty under the radar.

Uh so we use Atlas. We they were one of

our patch mates in YC.

They were maybe our first customer

actually and we've used them since they

started and vice versa.

>> What's the URL? Do you remember?

>> Uh atlas.so.so.

Oh, you guys got your So Mafia going?

>> Yeah,

>> it's Somalia as a domain name, right?

>> Yeah. Yeah, for sure.

So Zeus is cool because it doesn't

surface as a chatbot in the app. It's

just a live chat on our site and if you

ask me a question, it will actually

suggest things to me as an answer. And

then I can choose to revise my answer

based on the suggestions. Uh send it as

if it was sending from me. All of that.

So they never interface directly with an

AI. And anytime that I use anything,

it's always human in the loop. It's

something that I see, approve, and send

out.

>> And I I know you mentioned before you

bas you you personally onboarded the

first I don't know 300 customers for the

first year. I don't maybe maybe it's

even longer than that, but why did you

do that? Uh yeah, the entire uh year and

a half I did 100% of all boardings for

every new user. Um I think it's

important to understand what you're

building towards and what the market is.

If you don't like talking to lawyers,

you shouldn't build a legal company. If

you don't like talking to people

building software companies, you

shouldn't build a tool that caters to

them. So I I I do like this audience. I

I find the the aggregate level of tism

to be similar to my own

and it makes for for easy conversations

usually and

and I I find that we're still working

off of like the early Figma designs and

the early conversations that I had like

three and a half four years ago because

we fully understand this market, what

needs to be done, what needs to be

built.

>> Yeah, it's probably like you probably

learn a lot from your customers because

it's all it's like similar. you're all

building kind of like similar things, at

least more similar than someone who has

like a CPG brand or like an NFT thing.

Like it's software and like you're also

building a software company. Like just

talking to those people, you'll learn a

lot.

>> Yeah, you you you do. What I've learned

also is just how incredibly talented our

team is internally.

What I will typically find because we do

the support and we build the product,

we've gone toe-to-toe with many various

engineering departments and 95 96% of

the time our engineering team comes on

top with both like the solution of how

our data model is constructed and like

why it's a better solution

and these teams retain and they're happy

to build it and they tell the people

about it. So we we think it works.

>> Yeah. One of my one of my portfolio

companies, he describes it as you want

to compete against competitors where

they think of their engineering teams as

the IT department. Like they they don't

have engineering teams, they have they

have it where it's like that's that's

who you want to be competing against.

>> Absolutely. In in the software space

100%. Yeah.

>> Yeah. And you um speaking of like things

like 996, I feel like it's kind of in

the discourse like what I want that

whatever that means. I actually heard

you say you work seven days a week at

Loops. So that's like 997. So exp Ex

explain that. That sounds like that

sounds even more intense.

>> So I I have two kids, a 2-year-old and a

four-year-old actually just turned five.

And look, I'm I'm very plugged in. The

first thing I check

at in the morning is

inbox and Slack to make sure that like

customers aren't being held up, there's

not an issue in other way. I still do

probably 60 to 70% of all the support

myself.

I do all the onboarding still myself. We

don't we don't force onboarding, but I

do it all myself. And I am like the

point person for a lot of our larger

customers as well. Um, and like that's

all something that I've chosen and I'd

like to do and it's a place that I put

myself in on purpose. But as a result of

that, like you I do find myself working

probably more than most founders at my

at our current revenue level or team

size or whatever it happens to be.

A lot of that stuff can be unblocked on

my phone which is cool now but I still

for better or worse try to keep up with

the engineering team and it's just it

results in a lot of work. I am not like

996 though. I am like I am up when I'm

up and I'm looking at my phone and I am

on my computer often and then between

that is family and then there is pretty

much nothing else.

>> That's right. I mean, I feel like I'm in

the same boat where it'll be like like

you went to Disney World with the kids a

couple weekends ago. It's like a 4-day

trip over a long weekend. Super fun, but

you're definitely you're like in in a

ride about to get on like Guardian of

the Galaxy ride or whatever and like an

email and you're like, I got to quick

read this or something like you're

you're you're kind of working, but

you're also on vacation. It's like one

of those fluid things where I don't I

don't think I could ever actually fully

disconnect from anything. But also, I

don't work 24 hours a day, even though I

kind of do, if that makes sense.

>> Yeah, definitely. Like, absolutely.

Like, I might not be strapped in in

front of the laptop, but yeah, I mean,

like when I'm in the shower, right, I'm

like actively thinking about what the

next thing is for us, what I need to

discuss with people that day, like what

customer needs this and like it's it's

always on my mind. If it's on my own,

then my wife or my kids are and or other

members of my family. And like that's

what I have bandwidth for. It's one of

the reasons I can never move to San

Francisco and build this company. I just

don't I don't have the bandwidth for it.

There's not a world where I go to coffee

shops period. People are always like,

"Oh, the people you meet at coffee shop

like when are you going to like why do

you have the time to do that? Like what

are you doing?" Um, yeah, Michael Cybel

described it as like increasing your

luck surface area by living in a densely

populated place with many talented

people. But that only works if you

actually go somewhere. If you are just

like only building your company and it's

happening remotely and you're talking

and you're spending time with your

family and you're above the age of 30,

then like you do not have that time.

However, if you're under the age of 30

and you're in your 20s, then I think

it's a great place to build a company.

>> Yeah. I mean it's it's it's it's like in

one in one side it's like I always was I

I don't want to say hated but I did not

enjoy the sort of like political

small talk bureaucracy of like the

workplace of like you got to go hang out

in the kitchen and talk for 20 minutes

but it's like I got I got work to do and

like I got home 20 minutes later because

of this. But then in the other side it's

like you know it is useful to just like

combine work and your social life in the

same like I go to San Francisco a couple

days a month maybe like a week a month

and we'll have like uh host an event and

it's like kind of fun and you see some

friends but it's also like it's kind of

workrelated I guess like it all you kind

of hit it all in one shot to kill

multiple birds with one stone. So it's

like ah I get it.

>> Yeah it's it's reasonable. It's good.

I should probably do more of it. I just

when people talk about being locked in

and then they like also drink matchas

they don't make. I just don't understand

like how those two things coincide. Like

bro, you're not locked in. Like I've my

[ __ ] coffee makes itself in the

morning. I go downstairs, I drink it,

and I've already replied to like three

different things before I gotten out of

bed. Like like that that's locked in.

You know what I mean? Like I I I am

prematurely gray. I have like wild bags.

Like if you are lifting weights, you are

not locked in. You are lifting weights.

>> Have you seen that one video? It's like

the one guy who talks about how he does

three days in one day. Like he's like,

"When I wake up, I wake up at 6:00 a.m.

and I'm doing all this stuff by 12 by 12

p.m. I'm on my second day and by 4 p.m.

I start my third day and I do three

days. Like you give me a month, I'll

compete. You give me a year, I've lived

a lifetime." That's probably one of my

favorite videos. If you don't look like

you're dying of like some type of like

fatal illness, then you're probably not

as locked in.

Like you need to like honestly you

should look This is like the worst I've

looked in my life.

>> Really? I was going to say like Yeah,

you've got like the like the silver gray

almost like it looks good.

>> Thank you. I appreciate that. Yeah, like

genetically though that probably

shouldn't be happening. like stress,

like lack of sleep, children throwing

things at me.

>> Yeah, that's fair. Like, is it a bag or

is it just a bruise? Like, is it a bag

under the eye or did you get hit with a

like a block?

>> It's it's it could be either either or

depending on the day. But, you know,

like you see like like Sam like Sam's

not looking so good nowadays, right?

Like he's feeling it, you know? He's

doing it.

>> Yeah.

>> Yeah. Yeah. I want to see Show me those

podcasts where they don't look super

refined. Show me them like where they

look puffy. They look like like crap.

Elon always looks like [ __ ] Do you know

what I mean? Like you know that guy's

doing things. He looks terrible like a

100% of the time in like different ways,

you know? Like some days he's bloated,

some days he's like got like crazy bags

and all his hair is like like clearly

that guy has got some other stuff going

on that he just just this is like the

least important thing. You need to look

terrible to be successful.

>> So that's that's the thing is like if

you're if you're a founder, you're like

going you're doing your first CNBC

interview. Like, do you wear a suit? Do

you get a haircut? Do you get like a

manicure, like a face puffing, like some

kind of treatment before? Or do you go

on just looking like you got hit by a

truck? Like, what's the strategy?

>> I think you got to get a body double.

I'm not really sure there's any other

option. You need you need to like clone

a twin, have them trot out, like for all

the PR, all the fundraising around the

IPO. CNBC twin. It's the only solution.

>> So, this is somebody who looks really

good.

>> Yes. in your place in yourstead.

Absolutely. Yeah.

>> Interesting. Okay. I'll keep that in my

back pocket for when when I IPO the

Banana Capital and the Peele podcast

conglomerate in the future.

>> Sure. Yeah. I mean I mean why wouldn't

you? You should probably start working

on it now to be honest.

>> Probably. Yeah. One thing you mentioned

I I wanted to ask you about before we

signed off. You mentioned you recently

cleaned out a wasp nest with a shopvac.

I'm deathly afraid of of bees and wasps.

Like it's probably the one thing. It's

my irrational fear. like I just don't

like them. Like I just avoid putting

myself in those situations.

How do you do that? Like how do you how

do you clear out a wasp mess with a with

a shop back?

>> Yeah. I mean, you probably shouldn't.

One of the benefits of living in a small

town is that you start to feel

invigorated by some of your neighbors

doing things that they shouldn't do with

like on their exterior and stuff like

that. So like now I think I can do

pretty much anything. You know, these

hands are made for typing and that's

just what they do. But like every once

in a while like somebody will send me

text messages of something on Reddit

with like some homeowner thing which is

a friend of mine did and I was like I'm

doing this. So we had like a couple

hundred wasps that built a nest in one

of our walls.

>> Oh jeez. In inside the house or more

exterior?

>> We have like a secondary mudroom area.

So it's like borderline exterior

interior. Uh but you know they they had

breached the interior. So, they made it

into the secondary area and we had about

a dozen of them flying around inside

there and then hundreds in the walls.

So, my friend sent me a Reddit post and

I have a shop back. I filled it up with

some soap and water, taped it to a rake

and shoved it up into the hole and I I I

like vacuumed up maybe like a couple

hundred wasps just in a period of like

eight hours. Totally cleared it out.

Found another one on the other house the

other day. Did the same thing. Super

effective.

Yeah. And this weekend I'm like

chiseling a bunch of bricks in our

driveway just because it seems like

something I feel like I should be able

to do. Like you should be able to like

you should be able to chisel bricks.

>> Yeah. You got some confidence from the

the shop back.

>> Yeah. Yeah. Yeah. I looked online.

Apparently you can use a screwdriver

and like a large hammer. And I have both

those things. So

>> what are you trying to even out the

driveway or something? Like why do you

why do you chisel bricks in the

driveway?

>> We have this like we live in a nice

historic home. It's like 120 years old

or something. The bricks are just as old

as that and they have been pulverized in

like the front of our driveway like

these little pavers. They're basically

dust. So, they need to be like taken out

and then either flipped if they're not

totally pulverized or replaced. And it

means I also need to figure out how to

cut brick, which is something I will

figure out also.

>> Are you allowed to do this? Like, don't

they make laws like you can't change a

historic home? Like, you got to get

permits to do the smallest thing.

>> You can just do things. Yeah.

>> Oh, fair. It applies to startups and

historic homes.

>> Yeah. Yeah. Yeah. Yeah. Yeah. Ideally,

you do things with your car parked in

front of you so like the neighbors don't

see. But yeah, you can definitely do

things.

>> Yeah. Hopefully you don't have an HOA.

One of those Karens who's like reporting

everything.

>> No, no HOA. No HOA. We do have a a

neighborhood newsletter list who I've

tried to convince to use loops

unsuccessfully.

>> Okay.

>> I'm like somewhat on like the wrong side

of the fence there in terms of like my

early entrance into the community, but

I'm working on it. We'll see what

happens. Well, yeah. I mean, I think

that's probably a good way to end it.

Sounds like you have a lot to do this

weekend with the driveway, with the

chiseling, following up on the the bees

and the wasps, making sure you got them

all. Uh, but yeah, this is a lot of fun.

Is there is there any way people can

find you? Like Twitter, is that probably

best?

>> Yeah, I'm France Fries on Twitter. I'm

probably something on Reds and Blue Sky,

but I haven't checked in a year.

>> LinkedIn. Are you a LinkedIn guy?

>> I am not, but I am on there as Chris

France, I think. And if you don't get

me, you're going to get the drum over

the talking heads. So really, it's a win

no matter what.

>> Yeah. Didn't you say that? Someone

emails you all the time thinking that

that's who you are.

>> Yeah. Moby, a couple others people email

me thinking I'm the drum of the talking

heads because I own chrisance.com and

and yeah, it's cool. I mean, like I

almost like went to like a desert with

Moby. I just I had to bail and tell him

at the last moment that like I I'm not

Chris France. But like I really want to

meet Moby. Do you know what I mean? Like

I feel like he's like

>> just figure out a way. Yeah. Just just

go through with it one of these times

and be like, "Yeah, no. I'm I'm not

actually the drummer from the talking

heads. I'm just the the email software

guy."

>> Absolutely. Yeah. If you had used loops,

this confusion never would have

happened. Yeah.

>> Yeah. That's a really good marketing

pitch. Maybe you should try that for one

of your marketing stunts.

>> If we ever do a commercial, I'm going to

reply to that email and be like, "Hey,

Moby, like I need a soundtrack. Here's

$50,000. See, I told you I was a good

dude.

>> We'll be on the lookout for it. Maybe

we'll do a we'll do a follow-up episode

when you when you put out that first

commercial.

>> Perfect. Maybe I'll Maybe I'll Moi next

to me. That would be cool, right?

>> Yeah, that'll be awesome. Well, cool.

This is a lot of fun. Thanks for doing

it.

>> Yeah, for sure. Turn

>> and thank you for listening and thanks

to Handover Park and Ramp for supporting

this episode. Head to ramp.com/theappeal

for $250 on your first cards and

handover.com/turner

for the modern fund admin provider for

institutionalgrade investment firms. If

you like this conversation, check out

the back catalog of over 100 episodes,

including last week's with Dan Gray,

where we talk through untold lessons

from dozens of academic research papers

covering 40 years of startups and

venture capital. If you want to help me

out, please like, comment, subscribe,

and include me in the subject line of

your next customer email. If you want to

miss a future episode, subscribe to my

newsletter, The Split, linked at the

bottom of the description to get each

episode, plus a transcript, emailed

directly to your inbox every week.

Thanks again for listening. See you in

the next episode.

[Music]
