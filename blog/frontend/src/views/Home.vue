<template>
  <div class="home">
    <div v-for="article in articles" :key="article.id">
      <div>
        <h3>記事一覧</h3>
      </div>
      <div>
        <p>{{article.title}}</p>
        <span>{{article.createdAt.toDateString()}}</span>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import HelloWorld from '@/components/HelloWorld.vue';
import axios from 'axios';

interface ArticleDto {
  id: number;
  title: string;
  created_at: Date;
}

interface Article {
  id: number;
  title: string;
  createdAt: Date;
}

const convertDtoToArticle = (raw: ArticleDto): Article => ({
  id: raw.id,
  title: raw.title,
  createdAt: new Date(raw.created_at),
});

@Options({
  components: {
    HelloWorld,
  },
})
export default class Home extends Vue {
  articles: Article[] = []

  created() {
    axios.get('http://localhost:8000/api/blog/posts').then((response) => {
      console.log({
        a: 'ブログポスト一覧を取得した',
        response,
      });
      this.articles = response.data.map(convertDtoToArticle);
    }).catch((e) => {
      console.error(e);
    });
  }
}
</script>
