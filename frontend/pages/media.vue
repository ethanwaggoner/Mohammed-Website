<script setup lang="ts">
import { ref, computed } from 'vue';
import NavBarDark from "@/components/NavBarDark.vue";
import BottomBar from '@/components/BottomBar.vue';


const currentPage = ref(0);
const itemsPerPage = 3;

const images = [
  { src: '/images/media1.jpg', link: 'https://mediasite.citadel.edu/Mediasite/Play/bc28410fee634faea1eabc0f120b68301d' },
  { src: '/images/media2.jpg', link: 'https://www.jhunewsletter.com/article/2019/04/tedxjhu-speakers-challenge-societys-status-quo' },
  { src: '/images/media3.png', link: 'http://blog.ccbcmd.edu/khalid/2018/10/15/speaking-at-the-united-states-institute-of-peace-for-amate-symposium/' },
  { src: '/images/media4.jpg', link: 'https://www.heritage.org/terrorism/event/pathways-and-out-islamism-conversation-two-former-extremists' },
  { src: '/images/media5.jpg', link: 'https://worldfellows.yale.edu/event/deradicalization-united-states-discussion-former-usg-counterterrorism-analyst-and-former' },
  { src: '/images/media6.png', link: 'https://www.vice.com/en/article/vbwjqx/i-was-a-teenage-terrorist' },
  { src: '/images/media7.jpg', link: 'https://www.mohammedkhalid.com/blog/washington-post-magazines-cover-story-the-redemption-of-mohammed-khalid' },
  { src: '/images/media8.jpg', link: 'https://www.mohammedkhalid.com/blog/umbc-magazines-story-by-saving-one-life-you-have-saved-all-humankind' },
  { src: '/images/media9.jpg', link: 'https://mediasite.citadel.edu/Mediasite/Play/bc28410fee634faea1eabc0f120b68301d' }
];

const totalPages = computed(() => images.length);

const displayedImages = computed(() => {
  const start = currentPage.value % totalPages.value;
  const end = (start + itemsPerPage) % totalPages.value;
  if (end > start) {
    return images.slice(start, end);
  } else {
    return [...images.slice(start), ...images.slice(0, end)];
  }
});

const next = () => {
  currentPage.value = (currentPage.value + 1) % totalPages.value;
};

const prev = () => {
  currentPage.value = (currentPage.value - 1 + totalPages.value) % totalPages.value;
};
</script>

<template>
  <NavBarDark />

  <div class="media">
    <h1>Media Coverage (unclassified)</h1>
    <div class="color">
      <p>
        <span class="underline">DISCLAIMER:</span> I do not (and cannot) control the way how my case, experiences, or interviews are captured or portrayed. It is always quite regrettable to see how reality is sometimes either grossly exaggerated or understated. <span class="bold">Listed sources below are provided for reference, not accuracy.</span>
      </p>
    </div>
    <div class="carousel-container">
      <button @click="prev" class="carousel-control prev">&lt;</button>
      <div class="carousel">
        <div
          class="carousel-item"
          v-for="(image, index) in displayedImages"
          :key="index"
        >
          <a :href="image.link">
            <img :src="image.src" alt="Image Preview" />
          </a>
        </div>
      </div>
      <button @click="next" class="carousel-control next">&gt;</button>
    </div>
  </div>
   <div class="media-list">
    <p>Following is a brief list of unclassified media briefings and/or arrangements covering my advocacy and cases:</p>
    <p><em>Last updated: June 2, 2022</em></p>
    <ol>
      <li>
        Federal Bureau of Investigation. "BAU Training." <em>Behavioral Analysis Unit</em>, June 2, 2022, <a href="https://www.fbi.gov/">https://www.fbi.gov/</a>.
      </li>
      <li>
        New York City Police Department. "Virtual is Reality: Digital Drivers of Real World Harm." <em>NYPD's Fifth Annual Cyber Intelligence and Counterterrorism Conference</em>, 26 Aug. 2021, <a href="https://www.zecops.com/event/nypd-cyber-intelligence-and-counterterrorism-conference">https://www.zecops.com/event/nypd-cyber-intelligence-and-counterterrorism-conference</a>.
      </li>
      <li>
        Federal Bureau of Investigation. "BAU Symposium on Radicalization, Deradicalization, and Disengagement." <em>Behavioral Analysis Unit</em>, 12 Aug. 2021, <a href="https://www.fbi.gov/">https://www.fbi.gov/</a>.
      </li>
      <li>
        Rubin Museum of Art. "Radicalization on the Spectrum - Mohammed Khalid + Dr. Elizabeth Torres." <em>Brainwave 2021: Awareness</em>, 25 May 2021, <a href="https://rubinmuseum.org/events/event/brainwave-awareness-radicalization-on-the-spectrum">https://rubinmuseum.org/events/event/brainwave-awareness-radicalization-on-the-spectrum</a>.
      </li>
      <li>
        Community College of Baltimore County. "Alumni Spotlight: Mohammed Khalid, CCBC 2021 Graduate, Cybersecurity." <em>CCBC Alumni Spotlight</em>, 21 May 2021, <a href="https://www.ccbcmd.edu/Get-Started/Discover-CCBC/Our-Stories/Spotlight-alumni/Mohammed-Khalid.aspx">https://www.ccbcmd.edu/Get-Started/Discover-CCBC/Our-Stories/Spotlight-alumni/Mohammed-Khalid.aspx</a>.
      </li>
      <li>
        Fraser-Rahim, M. & Khalid, M., H. (2021). Deradicalization and rehabilitation: A case study of the Quilliam Foundation’s decade-long approach in the UK, the United States, and worldwide. In K. Bhui & D. Bhugra (Eds.), <em>Terrorism, Violent Radicalisation, and Mental Health</em> (First ed., Oxford Cultural Psychiatry Series, pp. 169-202). Oxford University Press. doi:10.1093/med/9780198845706.001.0001, <a href="https://global.oup.com/academic/product/terrorism-violent-radicalisation-and-mental-health-9780198845706">https://global.oup.com/academic/product/terrorism-violent-radicalisation-and-mental-health-9780198845706</a>.
      </li>
      <li>
        U.S. Department of Defense. "A Workshop on Domestic Extremism: Recruitment Overview and Live Panel Discussion with Deradicalized Individuals." <em>PERSEREC's Threat Lab</em>, 25 Mar. 2021, 6 May 2021, 27 May 2021, 16 Jun. 2021, 14 Jul. 2021, 11 Aug. 2021, <a href="https://www.eventleaf.com/DOMESTICEXTREMISMWORKSHOP">https://www.eventleaf.com/DOMESTICEXTREMISMWORKSHOP</a>.
      </li>
      <li>
        Leyshon, Randiannne. "By Saving One Life, You Have Saved All Humankind." <em>UMBC Magazine</em>, 18 Feb. 2021, <a href="https://magazine.umbc.edu/by-saving-one-life-you-have-saved-all-humankind">https://magazine.umbc.edu/by-saving-one-life-you-have-saved-all-humankind</a>.
      </li>
      <li>
        Powers, Ashley. "The Redemption of Mohammed Khalid." <em>The Washington Post Magazine</em>, 8 Feb. 2021, <a href="https://www.washingtonpost.com/magazine/2021/02/08/redemption-of-mohammed-khalid">https://www.washingtonpost.com/magazine/2021/02/08/redemption-of-mohammed-khalid</a>.
      </li>
      <li>
        May, Ashley. "Anti-Radical: When extremists leave prison, who helps them find a new life?" <em>PhilanthropyRoundtable</em>, 12 Apr. 2020, <a href="https://www.philanthropyroundtable.org/philanthropy-magazine/article/anti-radical">https://www.philanthropyroundtable.org/philanthropy-magazine/article/anti-radical</a>.
      </li>
      <li>
        Daily Signal News. "#522: Mohammed Khalid on Combating Islamist Extremism." <em>Apple Podcasts</em>, 9 Aug. 2019. <a href="https://podcasts.apple.com/ca/podcast/522-mohammed-khalid-on-combating-islamist-extremism/id1313611947?i=100046649949">https://podcasts.apple.com/ca/podcast/522-mohammed-khalid-on-combating-islamist-extremism/id1313611947?i=100046649949</a>.
      </li>
      <li>
        David, Daniel; Trinko, Katrina. "Youngest Person in US Prosecuted for Terrorism Now Fights Islamist Extremism." <em>The Daily Signal</em>, 9 Aug. 2019. <a href="https://www.dailysignal.com/2019/08/09/youngest-person-in-us-prosecuted-for-terrorism-now-fights-islamist-extremism">https://www.dailysignal.com/2019/08/09/youngest-person-in-us-prosecuted-for-terrorism-now-fights-islamist-extremism</a>.
      </li>
      <li>
        The Heritage Foundation. "Pathways in and out of Islamism: A Conversation with Two Former Extremists." <em>YouTube</em>, 16 Jul. 2019. <a href="https://youtu.be/2yuYuqjoWE">https://youtu.be/2yuYuqjoWE</a>.
      </li>
      <li>
        "Moderate Threat from Recently Released Terrorists." <em>State of New Jersey | Office of Homeland Security and Preparedness Analysis Bureau</em>, 24 May 2019. <a href="https://www.njhomelandsecurity.gov/analysis/moderate-threat-from-recently-released-terrorists">https://www.njhomelandsecurity.gov/analysis/moderate-threat-from-recently-released-terrorists</a>.
      </li>
      <li>
        TEDx Talks. "Reconciling Humanity: Struggles of a Former Teenage Terrorist | Mohammed Khalid | TEDxJHU." <em>YouTube</em>, 22 May 2019. <a href="https://youtu.be/4P1wq3QIa2I">https://youtu.be/4P1wq3QIa2I</a>.
      </li>
      <li>
        Cohen, Andrew. "Video of the Day: Mohammed Khalid was 17 years old when he was arrested and charged with conspiring to support terrorism. He was released from prison in 2017 and now is studying computer science and contributing to counterterrorism programs." <em>The Marshall Project</em>, 14 Mar. 2019. <a href="https://www.themarshallproject.org/records/7222-mohammed-khalid">https://www.themarshallproject.org/records/7222-mohammed-khalid</a>.
      </li>
      <li>
        "Citadel included in Vice News feature on reformed terrorist." <em>The Citadel</em>, 12 Mar. 2019. <a href="https://today.citadel.edu/citadel-vice-news-terrorist-cyber-intelligence">https://today.citadel.edu/citadel-vice-news-terrorist-cyber-intelligence</a>.
      </li>
      <li>
        VICE News. "I Was A Teenage Terrorist." <em>YouTube</em>, 12 Mar. 2019. <a href="https://youtu.be/tWJMIruJHU4">https://youtu.be/tWJMIruJHU4</a>.
      </li>
      <li>
        Caulderwood, Kathleen. "I was a teenage terrorist." <em>Vice</em>, 12 Mar. 2019. <a href="https://www.vice.com/en_us/article/vbwjqx/i-was-a-teenage-terrorist">https://www.vice.com/en_us/article/vbwjqx/i-was-a-teenage-terrorist</a>.
      </li>
      <li>
        The U.S. Department of Justice. "Government’s Sentencing Memorandum — United States of America v. Ali Charaf Damache." <em>GW Program on Extremism</em>, 23 Oct. 2018. <a href="https://extremism.gwu.edu/sites/g/files/zaxdzs2191/f/Damache%20Sentencing%20Memorandum.pdf">https://extremism.gwu.edu/sites/g/files/zaxdzs2191/f/Damache%20Sentencing%20Memorandum.pdf</a>.
      </li>
      <li>
        "Deradicalization in the United States: A Discussion with a Former USG Counterterrorism Analyst and a Former Jihadist/Islamist." <em>Yale Maurice R. Greenberg World Fellows Program</em>, 4 Oct. 2018. <a href="https://worldfellows.yale.edu/event/deradicalization-united-states-discussion-former-usg-counterterrorism-analyst-and-former">https://worldfellows.yale.edu/event/deradicalization-united-states-discussion-former-usg-counterterrorism-analyst-and-former</a>.
      </li>
      <li>
        "Moving on From Conviction: A Conversation with a Former Islamist and an Imam." <em>The Citadel — The Military College of South Carolina</em>, 25 Sep. 2018. <a href="https://mediasite.citadel.edu/Mediasite/Play/bc28410fee634faea1eabc0f120b68301d">https://mediasite.citadel.edu/Mediasite/Play/bc28410fee634faea1eabc0f120b68301d</a>.
      </li>
      <li>
        Kowalski, Daniel M. "CA2 on Derivative Citizenship: Khalid v. Sessions." <em>LexisNexis Legal NewsRoom</em>, 14 Sep. 2018. <a href="https://www.lexisnexis.com/legalnewsroom/immigration/b/insidenews/posts/ca2-on-derivative-citizenship-khalid-v-sessions">https://www.lexisnexis.com/legalnewsroom/immigration/b/insidenews/posts/ca2-on-derivative-citizenship-khalid-v-sessions</a>.
      </li>
      <li>
        Neumeister, Larry. "Court: Ex-terror defendant facing deportation is US citizen." <em>Associated Press News</em>, 13 Sep. 2018. <a href="https://apnews.com/cdc21b65f6f44c34b3f551cebfcf729f">https://apnews.com/cdc21b65f6f44c34b3f551cebfcf729f</a>.
      </li>
      <li>
        Klasfeld, Adam. "Making Amends, Ex-Teen Terrorist Becomes US Citizen." <em>Courthouse News Service</em>, 13 Sep. 2018. <a href="https://www.courthousenews.com/making-amends-ex-teen-terrorist-becomes-us-citizen">https://www.courthousenews.com/making-amends-ex-teen-terrorist-becomes-us-citizen</a>.
      </li>
      <li>
        Hamilton, Colby. "2nd Circuit Says Citizenship Can't Be Stripped Over Pretrial Detention in Terror Case." <em>Law.com | New York Law Journal</em>, 13 Sep. 2018. <a href="https://www.law.com/newyorklawjournal/2018/09/13/2nd-circuit-says-citizenship-cant-be-stripped-over-pretrial-detention-in-terror-case">https://www.law.com/newyorklawjournal/2018/09/13/2nd-circuit-says-citizenship-cant-be-stripped-over-pretrial-detention-in-terror-case</a>.
      </li>
      <li>
        "In and Out of Extremism USA." <em>Quilliam</em>, 4 Jun. 2018. <a href="https://www.quilliaminternational.com/shop/e-publications/in-and-out-of-extremism-usa">https://www.quilliaminternational.com/shop/e-publications/in-and-out-of-extremism-usa</a>.
      </li>
      <li>
        Taylor, David. "He was a teenage terrorist. Now he’s fighting extremism." <em>The Guardian</em>, 3 Jun. 2018. <a href="https://www.theguardian.com/us-news/2018/jun/03/mohammed-khalid-america-youngest-terrorist-interview">https://www.theguardian.com/us-news/2018/jun/03/mohammed-khalid-america-youngest-terrorist-interview</a>.
      </li>
      <li>
        "Why People Join Extremist Groups." <em>American Muslims Against Terrorism & Extremism</em>, 8 Mar. 2018. <a href="https://www.amateinitiative.com/why_people_join_extremist_groups">https://www.amateinitiative.com/why_people_join_extremist_groups</a>.
      </li>
      <li>
        "Youth and Countering Violent Extremism." <em>American Muslims Against Terrorism & Extremism</em>, 8 Mar. 2018. <a href="https://www.amateinitiative.com/youth_and_countering_violent_extremism">https://www.amateinitiative.com/youth_and_countering_violent_extremism</a>.
      </li>
      <li>
        Immigrant Defense Project. "Brief of Amici Curiae Center For Family Representation, Her Justice, Sanctuary For Families, The Door’s Legal Services Center, Columbia Law School Immigrants' Rights Clinic, Immigrant Rights Clinic at NYU School of Law, Kathryn O. Greenberg Immigration Justice Clinic at Benjamin N. Cardozo School of Law, Brooklyn Defender Services, Monroe County Public Defender’s Office, Neighborhood Defender Service of Harlem, New York County Defender Services, The Bronx Defenders, The Legal Aid Society, Center for Constitutional Rights, Immigrant Defense Project, and Professors Chris Gottlieb, Kim Taylor-Thompson, Martin Guggenheim, Michael Wishnie, Randy Hertz, and Tony Thompson in Support of Petitioner and in Support of Granting the Petition for Review." <em>Immigrant Defense Project</em>, 24 Jun. 2017. <a href="https://www.immigrantdefenseproject.org/wp-content/uploads/Brief-of-Amici-Curiae-No.-16-3480-Khalid-v-Sessions_Redacted.pdf">https://www.immigrantdefenseproject.org/wp-content/uploads/Brief-of-Amici-Curiae-No.-16-3480-Khalid-v-Sessions_Redacted.pdf</a>.
      </li>
      <li>
        Shiffman, John. "U.S judge says terrorism convict can't be deported to Pakistan." <em>Reuters</em>, 16 Apr. 2016. <a href="https://www.reuters.com/article/us-usa-jihadjane-khalid-idUSKCN0XD0X2">https://www.reuters.com/article/us-usa-jihadjane-khalid-idUSKCN0XD0X2</a>.
      </li>
      <li>
        Duncan, Ian. "Ellicott City man sentenced for terrorism offenses." <em>Baltimore Sun</em>, 17 Apr. 2014. <a href="https://www.baltimoresun.com/maryland/bs-md-terror-sentencing-20140417-story.html">https://www.baltimoresun.com/maryland/bs-md-terror-sentencing-20140417-story.html</a>.
      </li>
      <li>
        Loeb, Pat. "Man Sentenced For Role — As A Teen — In Jihad Jane Terror Case." <em>CBS Philly</em>, 17 Apr. 2014. <a href="https://philadelphia.cbslocal.com/2014/04/17/man-sentenced-for-role-as-a-teen-in-jihad-jane-terror-case">https://philadelphia.cbslocal.com/2014/04/17/man-sentenced-for-role-as-a-teen-in-jihad-jane-terror-case</a>.
      </li>
      <li>
        Pilkington, Ed. "Mohammad Hassan Khalid given five years in jail for his part in jihadist plot." <em>The Guardian</em>, 17 Apr. 2014. <a href="https://www.theguardian.com/world/2014/apr/17/mohammad-hassan-khalid-sentence-five-years-jail-jihad-jane-plot">https://www.theguardian.com/world/2014/apr/17/mohammad-hassan-khalid-sentence-five-years-jail-jihad-jane-plot</a>.
      </li>
      <li>
        Roebuck, Jeremy. "Teen in 'Jihad Jane' plot gets 5 years in prison." <em>Inquirer.com</em>, 17 Apr. 2014. <a href="https://www.inquirer.com/philly/news/breaking/20140418_Teen_in__Jihad_Jane__plot_gets_5_years__prison.html">https://www.inquirer.com/philly/news/breaking/20140418_Teen_in__Jihad_Jane__plot_gets_5_years__prison.html</a>.
      </li>
      <li>
        Metcalf, Andrew. "Prosecutors Request 10 Years for Ellicott City Teen who Aided Terrorist Group." <em>Patch</em>, 6 Jan. 2014. <a href="https://patch.com/maryland/ellicottcity/prosecutors-request-10-years-for-ellicott-city-teen-who-aided-terrorist-group">https://patch.com/maryland/ellicottcity/prosecutors-request-10-years-for-ellicott-city-teen-who-aided-terrorist-group</a>.
      </li>
      <li>
        Spencer, Saranac H. "Teenage Terrorist Wants Transfer to State-Run Facility." <em>Law.com | The Legal Intelligencer</em>, 12 Jun. 2012. <a href="https://www.law.com/thelegalintelligencer/almID/1202559044844">https://www.law.com/thelegalintelligencer/almID/1202559044844</a>.
      </li>
      <li>
        Associated Press. "Mohammad Hassan Khalid seeks move to juvenile facility". <em>The Washington Post</em>, 12 Jun. 2012. <a href="https://www.washingtonpost.com/blogs/crime-scene/post/mohammad-hassan-khalid-seeks-move-to-juvenile-facility/2012/06/12/gJQADSSFXV_blog.html">https://www.washingtonpost.com/blogs/crime-scene/post/mohammad-hassan-khalid-seeks-move-to-juvenile-facility/2012/06/12/gJQADSSFXV_blog.html</a>.
      </li>
      <li>
        Department of Justice | Office of Public Affairs. "Maryland Man Pleads Guilty to Conspiracy to Provide Material Support to Terrorists." <em>The United States Department of Justice</em>, 4 May 2012. <a href="https://www.justice.gov/opa/pr/maryland-man-pleads-guilty-conspiracy-provide-material-support-terrorists">https://www.justice.gov/opa/pr/maryland-man-pleads-guilty-conspiracy-provide-material-support-terrorists</a>.
      </li>
      <li>
        Daily Mail Reporter. "Maryland terror teen who dreamed of joining Al Qaeda pleads guilty to web conspiracy with blue-eyed 'Jihad Jane'." <em>Daily Mail Online</em>, 4 May 2012. <a href="https://www.dailymail.co.uk/news/article-2139852/Maryland-terror-teen-dreamed-joining-Al-Qaeda-pleads-guilty-web-conspiracy-blue-eyed-Jihad-Jane.html">https://www.dailymail.co.uk/news/article-2139852/Maryland-terror-teen-dreamed-joining-Al-Qaeda-pleads-guilty-web-conspiracy-blue-eyed-Jihad-Jane.html</a>.
      </li>
      <li>
        Shiffman, John. "Honor student pleads guilty in Jihad Jane plot." <em>Reuters</em>, 4 May 2012. <a href="https://www.reuters.com/article/us-jihadjane/honor-student-pleads-guilty-in-jihad-jane-plot-idUSBRE8431GJ20120504">https://www.reuters.com/article/us-jihadjane/honor-student-pleads-guilty-in-jihad-jane-plot-idUSBRE8431GJ20120504</a>.
      </li>
      <li>
        Gedalyahu, Tzvi B. "US Teenage Muslim Charged in 'Jihad Jane' Plot." <em>Arutz Sheva 7</em>, 24 Oct. 2011. <a href="https://www.israelnationalnews.com/News/News.aspx/149024">https://www.israelnationalnews.com/News/News.aspx/149024</a>.
      </li>
      <li>
        Aseerun. "FBI Charges Mohammed Khalid for Actions that Allegedly Occurred while still a Minor (15)." <em>Aseerun</em>, 29 Oct. 2011. <a href="https://aseerun.wordpress.com/2011/10/29/fbi-charges-mohammed-khalid-for-actions-that-allegedly-occurred-while-still-a-minor-15">https://aseerun.wordpress.com/2011/10/29/fbi-charges-mohammed-khalid-for-actions-that-allegedly-occurred-while-still-a-minor-15</a>.
      </li>
      <li>
        Gedalyahu, Tzvi B. "US Teenage Muslim Charged in 'Jihad Jane' Plot." <em>Arutz Sheva 7</em>, 24 Oct. 2011. <a href="https://www.israelnationalnews.com/News/News.aspx/149024">https://www.israelnationalnews.com/News/News.aspx/149024</a>.
      </li>
      <li>
        Shiffman, John. "18-year-old charged in 'Jihad Jane' terror case." <em>The Philadelphia Inquirer</em>, 21 Oct. 2011. <a href="https://www.inquirer.com/philly/news/homepage/20111021_18-year-old_charged_in__quot_Jihad_Jane_quot__terror_case.html">https://www.inquirer.com/philly/news/homepage/20111021_18-year-old_charged_in__quot_Jihad_Jane_quot__terror_case.html</a>.
      </li>
      <li>
        U.S. Department of Justice | Office of Public Affairs. "Two Indicted for Conspiracy to Provide Material Support to Terrorists." <em>The Federal Bureau of Investigation</em>, 20 Oct. 2011. <a href="https://archives.fbi.gov/archives/philadelphia/press-releases/2011/two-indicted-for-conspiracy-to-provide-material-support-to-terrorists">https://archives.fbi.gov/archives/philadelphia/press-releases/2011/two-indicted-for-conspiracy-to-provide-material-support-to-terrorists</a>.
      </li>
    </ol>
  </div>

  <BottomBar />
</template>

<style scoped>
.media {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
}

.color {
  background-color: #dda758;
  width: 100%;
}

h1 {
  font-size: 3em;
  margin: 5%;
}

p {
  font-size: 1.5em;
  margin: 10%;
}

.underline {
  text-decoration: underline;
}

.bold {
  font-weight: bold;
}

.carousel-container {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 20px;
  width: 100%;
  padding: 20px;
  box-sizing: border-box;
}

.carousel {
  display: flex;
  overflow: hidden;
  width: 80%;
}

.carousel-item {
  flex: 0 0 33.3333%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 10px;
  box-sizing: border-box;
}

.carousel-item img {
  width: 100%;
  height: 400px;
  object-fit: cover;
  border-radius: 10px;
}

.carousel-control {
  background: none;
  border: none;
  font-size: 2em;
  cursor: pointer;
  color: darkorange;
}

.carousel-control:hover {
  color: black;
}

.media-list {
  margin: 0 20% 0 20%;
  font-size: 20px;
}

.media-list p {
  font-size: 1.2em;
  margin: 10px;
}

.media-list em {
  font-style: italic;
}

.media-list a {
  text-decoration: underline;
}

.media-list ol {
  margin-left: 20px;
}

.media-list li {
  margin-bottom: 10px;
}
</style>
