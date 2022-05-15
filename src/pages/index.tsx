import React from 'react';
import clsx from 'clsx';
import Layout from '@theme/Layout';
import Translate ,{translate} from "@docusaurus/Translate";
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import styles from './index.module.css';
import HomepageFeatures from '@site/src/components/HomepageFeatures';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <h1 className={clsx("hero__title",styles.heroTitle)}>{siteConfig.title}</h1>
        <p className={clsx("hero__subtitle",styles.heroSubtitle)}>{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link
            className={
              clsx("button button--outline button--primary,button--lg")
            }
            to="/docs/intro">
            <Translate>Let's Do it Daily!</Translate>
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home(): JSX.Element {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={translate({message:"Python Daily for QA"})}
      description={translate({message:"每一天一个微小进步，让你更了解python，更好自动化自己的日常任务！"})}>
      <HomepageHeader />
      <main>
        <HomepageFeatures />
      </main>
    </Layout>
  );
}
