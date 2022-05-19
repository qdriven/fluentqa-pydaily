import React from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';
import Translate ,{translate} from "@docusaurus/Translate";

type FeatureItem = {
  title: string;
  Svg: React.ComponentType<React.ComponentProps<'svg'>>;
  description: JSX.Element;
};

const FeatureList: FeatureItem[] = [
  {
    title: translate({message:"Python Tips for QA"}),
    Svg: require('@site/static/img/undraw_docusaurus_mountain.svg').default,
    description: (
        <Translate>
            python 常用方法介绍，让QA更了解python的使用
        </Translate>
        ),
  },
  {
    title: translate({message: "更现代的Python"}),
    Svg: require('@site/static/img/undraw_docusaurus_tree.svg').default,
    description: (
        <Translate>
            Python更现代的用法，类型和动态特征并重，随性和设计模式兼顾！
        </Translate>
    ),
  },
  {
    title: translate({message:"用python更多自动化"}),
    Svg: require('@site/static/img/undraw_docusaurus_react.svg').default,
    description: (
        <Translate>
            更多自动化的实践，让您把python用在实处！
        </Translate>
    ),
  },
];

function Feature({title, Svg, description}: FeatureItem) {
  return (
    <div className={clsx('col col--4',styles.features)}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <h3 className={styles.featureTitle}>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): JSX.Element {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
