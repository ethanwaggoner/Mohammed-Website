<script setup>
import NavBar from "~/components/NavBar.vue";
import BottomBar from "~/components/BottomBar.vue";
</script>

<template>
  <div class="background">
    <NavBar />
    <div class="container">
      <div class="content">
        <blockquote>
          “A person’s tongue can give you the taste of his heart.” -- Ibn Qayyim al-Jawziyya (r.a.)
        </blockquote>
        <p>
          Mo’s Notes is an avenue to share my occasional ruminations and creative works (fictionalized accounts, hazy poems, and such) with the world. Like many of you, I am always in a journey of finding and discovering my place in this beautiful yet transitory world of ours that God gave us. As no written piece can fully capture the depths of human experience, this site itself is a puzzle for me to know and for you to find out (though I’m happy to be <a href="#">available</a> for any clarifications). For now, we shall claim:
        </p>
        <h1>
          Mo’s Notes is a provisional place to share one man’s random thoughts within the context of his life and experiences.
        </h1>
        <h2><em>Biography:</em></h2>
        <p>
          Mohammed Khalid is a lifelong learner, cybersecurity consultant, business analyst, author and public speaker. His visionary perspective has earned him opportunities to work with global organizations, governments, community, and local actors towards an open society when developing holistic and contextualized counterextremism policies and initiatives. He has been featured on many outlets, including <em>The Washington Post Magazine, The Daily Signal, The Guardian, UMBC Magazine</em>, and others.
        </p>
        <p>
          Mohammed holds a master’s degree in Security Informatics from Johns Hopkins University, where he was also an Information Security Institute fellow. He received his bachelor of science, <em>magna cum laude</em>, in Information Systems from University of Maryland, Baltimore County as a Cyber Scholar with an Honors College Certificate. His previous appointments include serving as an Albrecht Fellow at the World Trade Center Institute, an IT Lab: SSI Fellow at Carnegie Mellon, and an i3 Scholar at the University of Pittsburgh.
        </p>
        <p>
          Mohammed regularly shares his experiences on his website, <a href="http://mohammedkhalid.com">mohammedkhalid.com</a>.
        </p>
      </div>
    </div>
  </div>
    <div class="additional-section">
      <img src="@/assets/aboutSelfie.jpg" alt="Mohammed Khalid" class="profile-image">
      <div class="additional-content">
        <p>
          Mohammed works from Washington, DC and is available to travel for speaking engagements.
        </p>
        <p>
          To learn more, contact him here:
        </p>
        <NuxtLink to="/contact"><button class="contact-button">Contact Mohammed</button></NuxtLink>
      </div>
    </div>
  <BottomBar />
</template>

<style scoped>
.background {
  background-color: #dda758;
  padding-bottom: 10%;
}
.container {
  color: #000;
  font-family: 'Times New Roman', 'serif';
  padding: 20px;
  line-height: 1.6;
  margin: 0 auto;
  max-width: 80%;
}

.content {
  margin: 0 10%;
}

blockquote {
  font-style: italic;
  text-align: right;
  margin: 20px 0;
  border-left: 5px solid #fff;
  padding-left: 20px;
}

h1 {
  font-size: 2.5em;
  margin: 20px 0;
}

h2 {
  font-size: 1.5em;
  font-style: italic;
  margin-top: 30px;
}

p {
  font-size: 1.25em;
}

a {
  color: #000;
  text-decoration: underline;
}

.additional-section {
  display: flex;
  align-items: center;
  background-color: #fff;
  padding-top: 10%;
  margin: 0 auto;
  max-width: 60%;
}

.profile-image {
  max-width: 40%;
  height: auto;
  margin-right: 20px;
}

.additional-content {
  text-align: center;
  margin-left: 10%;
}

.additional-content p {
  font-size: 1.5em;
  margin: 20px 0;
}

.contact-button {
  background-color: #000;
  color: #fff;
  border: none;
  padding: 10px 20px;
  font-size: 1.25em;
  cursor: pointer;
  margin-top: 20px;
}
</style>
