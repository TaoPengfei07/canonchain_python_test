FROM registry.cn-hangzhou.aliyuncs.com/canonchain/czr:ci as czr

FROM registry.cn-hangzhou.aliyuncs.com/canonchain/czr_tester:ci

COPY --from=czr /usr/local/bin /usr/local/bin

ARG branch=master
ARG ssh_key
ARG ssh_pub_key

#add SSH keys
RUN mkdir -p /root/.ssh \
    && echo "$ssh_key" > /root/.ssh/id_rsa \
    && echo "$ssh_pub_key" > /root/.ssh/id_rsa.pub \
    && chmod -R 600 /root/.ssh/id_rsa \
    && chmod -R 600 /root/.ssh/id_rsa.pub \
    && ssh-keyscan -H e.coding.net >> /root/.ssh/known_hosts

RUN git clone -b $branch git@e.coding.net:canonchain/rpc_api_test.git --recursive
	
COPY do_rpc_api_test.py ./

#Do test
CMD ["python", "do_rpc_api_test.py"]
